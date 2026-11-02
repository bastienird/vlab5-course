#!/usr/bin/env python3
import os, re, sys, argparse, html, json, zipfile
from pathlib import Path

def read_titles_from_search_json(search_json: Path) -> dict:
    title_map = {}
    if search_json.exists():
        try:
            data = json.loads(search_json.read_text(encoding="utf-8"))
            for entry in data:
                href = entry.get("href", "")
                title = (entry.get("title") or "").strip()
                if href and title:
                    title_map[href] = title
        except Exception:
            pass
    return title_map

def first_heading_from_md(md_path: Path) -> str:
    try:
        for line in md_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\s*#{1,6}\s+(.+?)\s*$", line)
            if m:
                return m.group(1).strip()
    except Exception:
        pass
    return md_path.stem.replace("-", " ").replace("_", " ").title()

def humanize_name(p: Path) -> str:
    return p.stem.replace("-", " ").replace("_", " ").title()

def main():
    ap = argparse.ArgumentParser(description="Build IMS Content Package from .md or .html files")
    ap.add_argument("--src", required=True, help="Dossier source (ex: md_out ou docs/solo)")
    ap.add_argument("--ext", choices=["md","html"], required=True, help="Extension à empaqueter")
    ap.add_argument("--outzip", default="moodle_ims_package.zip", help="Nom du .zip de sortie")
    ap.add_argument("--exclude", nargs="*", default=["index.html","about.html","about.md","search.json"],
                    help="Noms à exclure")
    ap.add_argument("--prefix-numbers", action="store_true",
                    help="Préfixer numériquement les items (01-, 02-, …)")
    ap.add_argument("--rename-safe", dest="rename_safe", action="store_true",
                    help="Renommer en interne (remplacer espaces, &, %) pour éviter les soucis")
    args = ap.parse_args()

    src = Path(args.src).resolve()
    if not src.is_dir():
        print(f"❌ Source introuvable : {src}", file=sys.stderr); sys.exit(1)

    work = Path("ims_pkg")
    if work.exists():
        for p in work.glob("*"):
            if p.is_dir():
                for q in p.rglob("*"): q.unlink()
                p.rmdir()
            else:
                p.unlink()
        work.rmdir()
    work.mkdir()

    files = []
    for p in sorted(src.iterdir()):
        if not p.is_file(): 
            continue
        if p.name in args.exclude: 
            continue
        if p.suffix.lower().lstrip(".") != args.ext:
            continue
        files.append(p)

    if not files:
        print("❌ Aucun fichier à empaqueter.", file=sys.stderr); sys.exit(1)

    title_map = {}
    if args.ext == "html":
        search_json = Path("docs") / "search.json"
        title_map = read_titles_from_search_json(search_json)

    copied = []
    for idx, src_file in enumerate(files, start=1):
        if args.rename_safe:
            safe = re.sub(r"[&]", "and", src_file.name)
            safe = re.sub(r"\s+", "-", safe)
            safe = safe.replace("%", "pct")
            dst_name = safe
        else:
            dst_name = src_file.name
        if args.prefix_numbers:
            dst_name = f"{idx:02d}-{dst_name}"
        dst = work / dst_name
        dst.write_bytes(src_file.read_bytes())
        copied.append(dst.name)

    items_xml, res_xml = [], []
    for i, fname in enumerate(copied, start=1):
        item_id = f"ITEM{i}"
        res_id  = f"RES{i}"
        href_safe = html.escape(fname)

        title_guess = ""
        if args.ext == "html":
            title_guess = title_map.get(fname) or title_map.get(Path(fname).name) or ""
        if not title_guess:
            if args.ext == "md":
                title_guess = first_heading_from_md(work / fname)
            else:
                title_guess = humanize_name(Path(fname))
        title_safe = html.escape(title_guess)

        items_xml.append(
            f'      <item identifier="{item_id}" identifierref="{res_id}">\n'
            f'        <title>{title_safe}</title>\n'
            f'      </item>'
        )
        res_xml.append(
            f'    <resource identifier="{res_id}" type="webcontent" href="{href_safe}">\n'
            f'      <file href="{href_safe}"/>\n'
            f'    </resource>'
        )

    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="vlab5-course" xmlns="http://www.imsglobal.org/xsd/imscp_v1p1">
  <organizations default="ORG1">
    <organization identifier="ORG1" structure="hierarchical">
{os.linesep.join(items_xml)}
    </organization>
  </organizations>
  <resources>
{os.linesep.join(res_xml)}
  </resources>
</manifest>
'''
    (work / "imsmanifest.xml").write_text(manifest, encoding="utf-8")

    outzip = Path(args.outzip).resolve()
    with zipfile.ZipFile(outzip, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for name in copied:
            z.write(work / name, arcname=name)
        z.write(work / "imsmanifest.xml", arcname="imsmanifest.xml")

    print(f"✅ IMS package créé : {outzip}")
    print(f"   Contenu : {len(copied)} items ({args.ext}) depuis {src}")
    print("   Import Moodle : Ajouter activité → Paquet de contenu IMS")

if __name__ == "__main__":
    main()
