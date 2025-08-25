
to render website and .md : 

``` bash
# 1) Site web complet pour GitHub Pages
quarto render
```

``` bash
# The other ones
bash build_all.sh 

```

``` bash
python3 md_to_moodle_codeblocks.py \
  --src md_out \
  --dst md_moodle
```
