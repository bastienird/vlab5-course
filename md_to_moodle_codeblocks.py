#!/usr/bin/env python3
import argparse, html, re
from pathlib import Path

LABEL_MAP = {
    "r": "R", "rscript": "R", "rmd": "R",
    "bash": "Bash", "sh": "Bash", "zsh": "Bash", "shell": "Bash",
    "python": "Python", "py": "Python",
    "sql": "SQL", "yaml": "YAML", "json": "JSON",
    "html": "HTML", "xml": "XML",
    "dockerfile": "Dockerfile", "docker": "Dockerfile",
}

INDENT_RE = re.compile(r"^(?: {4,}|\t)")  # ligne “verbatim” (≥4 espaces ou 1 tab)

def strip_top_title(md_text: str) -> str:
    lines = md_text.splitlines()
    i, n = 0, len(lines)

    # 1) Front matter YAML éventuel au tout début
    if i < n and lines[i].strip() == "---":
        j = i + 1
        while j < n and lines[j].strip() != "---":
            j += 1
        if j < n and lines[j].strip() == "---":
            i = j + 1  # saute le bloc YAML

    # Sauter lignes vides initiales
    while i < n and lines[i].strip() == "":
        i += 1

    # 2) Titre H1 de type ATX: "# Mon titre"
    if i < n and lines[i].lstrip().startswith("#"):
        i += 1
        while i < n and lines[i].strip() == "":
            i += 1
        return "\n".join(lines[i:]) + ("\n" if md_text.endswith("\n") else "")

    # 3) Titre H1 de type Setext:
    #    Mon titre
    #    ========
    if i + 1 < n and lines[i].strip() and re.match(r"^\s*=+\s*$", lines[i + 1]):
        i += 2
        while i < n and lines[i].strip() == "":
            i += 1
        return "\n".join(lines[i:]) + ("\n" if md_text.endswith("\n") else "")

    # Sinon, inchangé
    return md_text


def parse_lang(token: str) -> str:
    if not token:
        return ""
    token = token.strip()
    if token.startswith("{") and "}" in token:  # ex: {r, echo=FALSE}
        token = token[1:token.index("}")]
    return token.split()[0].lower()

def render_code_block(code_lines, lang, add_label=True):
    label_txt = LABEL_MAP.get(lang, (lang.upper() if lang else "Code"))
    css_lang = lang if lang else "text"
    code_text = "\n".join(code_lines)
    code_escaped = html.escape(code_text, quote=False)
    parts = []
    if add_label:
        parts.append(f"<p><strong>{label_txt} code:</strong></p>")
    parts.append(f'<pre><code class="language-{css_lang}">\n{code_escaped}\n</code></pre>')
    return parts

def render_output_block(out_lines, add_label=True):
    # Nettoie une 1re indentation commune (4 espaces / tab) pour aérer
    cleaned = []
    for ln in out_lines:
        if ln.startswith("\t"):
            cleaned.append(ln[1:])
        elif ln.startswith("    "):
            cleaned.append(ln[4:])
        else:
            cleaned.append(ln)
    text = "\n".join(cleaned)
    text_escaped = html.escape(text, quote=False)
    parts = []
    if add_label:
        parts.append("<p><strong>Output:</strong></p>")
    parts.append(f'<pre><code class="language-text">\n{text_escaped}\n</code></pre>')
    return parts

def transform(md_text: str, add_label: bool, capture_output: bool) -> str:
    lines = md_text.splitlines()
    out = []
    in_code = False
    lang = ""
    buf = []
    i = 0
    N = len(lines)

    while i < N:
        line = lines[i]
        stripped = line.lstrip()

        # ouverture code fence
        if not in_code and stripped.startswith("```"):
            after = stripped[3:].strip()
            lang = parse_lang(after)
            in_code = True
            buf = []
            i += 1
            continue

        # fermeture code fence
        if in_code and stripped.startswith("```"):
            # rendu du bloc de code
            out.extend(render_code_block(buf, lang, add_label=add_label))
            in_code = False
            lang = ""
            buf = []

            # option : capturer un bloc “output” immédiatement après (lignes indentées)
            if capture_output:
                j = i + 1
                out_buf = []
                # sauter une éventuelle ligne vide juste après
                if j < N and lines[j].strip() == "":
                    j += 1
                # capturer tant que lignes indentées (≥4 espaces ou tab)
                while j < N and (INDENT_RE.match(lines[j]) or lines[j].strip() == "" and (j+1 < N and INDENT_RE.match(lines[j+1]))):
                    out_buf.append(lines[j])
                    j += 1
                if out_buf:
                    out.extend(render_output_block(out_buf, add_label=add_label))
                    i = j
                    continue

            i += 1
            continue

        # à l’intérieur d’un bloc de code
        if in_code:
            buf.append(line)
            i += 1
            continue

        # hors code : recopier tel quel
        out.append(line)
        i += 1

    # bloc non fermé (rare) → on le ferme proprement
    if in_code:
        out.extend(render_code_block(buf, lang, add_label=add_label))

    return "\n".join(out) + "\n"

def main():
    ap = argparse.ArgumentParser(description="Convertit ```lang en <pre><code> et capture l'output indenté pour Moodle")
    ap.add_argument("--src", default="md_out", help="Dossier source .md (par défaut: md_out)")
    ap.add_argument("--dst", default="md_moodle", help="Dossier de sortie (par défaut: md_moodle)")
    ap.add_argument("--no-label", action="store_true", help="Ne pas ajouter les labels 'X code:' / 'Output:'")
    ap.add_argument("--no-output", action="store_true", help="Ne pas capturer l'output indenté après les blocs")
    ap.add_argument("--keep-title", action="store_true",
                help="Conserver le premier titre (# ... / Setext) au lieu de le retirer")
    args = ap.parse_args()

    src = Path(args.src)
    dst = Path(args.dst)
    dst.mkdir(parents=True, exist_ok=True)

    md_files = sorted(src.glob("*.md"))
    if not md_files:
        print(f"❌ Aucun .md trouvé dans {src.resolve()}")
        return
    for p in md_files:
        txt = p.read_text(encoding="utf-8")
    
        if not args.keep_title:
            txt = strip_top_title(txt)  # <-- retire le front-matter et le H1 de tête
    
        converted = transform(
            txt,
            add_label=not args.no_label,
            capture_output=not args.no_output
        )
        (dst / p.name).write_text(converted, encoding="utf-8")
        print(f"✔︎ {p.name} → {dst/p.name}")


if __name__ == "__main__":
    main()
