
to render website and .md : 

``` bash
# 1) Site web complet pour GitHub Pages
quarto render

# 2) Pages HTML “solo” (une page autonome par .qmd) -> docs/solo/
quarto render --profile solo

# 3) Markdown GFM pour Moodle (copier-coller facile) -> md_out/
quarto render --profile md --to gfm --output-dir md_out --no-cache

```

``` bash
python3 md_to_moodle_codeblocks.py \
  --src md_out \
  --dst md_moodle
```

# 
# 
# ``` bash
# quarto render . --to gfm --output-dir md_out
# ```
# 
# ``` bash
# quarto render --profile solo
# ```
# 
