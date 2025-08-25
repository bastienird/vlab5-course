#!/bin/bash

set -e  # stop if error

echo "🌐 Rendering main site..."
quarto render

# ----- SOLO -----
echo "🔧 Rendering SOLO..."
mkdir -p temp-solo
cp _quarto-solo.yml temp-solo/_quarto.yml
cp *.qmd temp-solo/

quarto render temp-solo --no-cache
mkdir -p docs/solo
cp -r temp-solo/solo_build/* docs/solo/
rm -rf temp-solo

# ----- MARKDOWN -----
echo "📝 Rendering MARKDOWN..."
mkdir -p temp-md
cp _quarto-md.yml temp-md/_quarto.yml
cp *.qmd temp-md/

quarto render temp-md --no-cache
mkdir -p md_out
cp -r temp-md/md_out/* md_out/
rm -rf temp-md

# ----- HTML LIGHT -----
echo "💡 Rendering HTML LIGHT..."
mkdir -p temp-light
cp _quarto-light.yml temp-light/_quarto.yml
cp *.qmd temp-light/

quarto render temp-light --no-cache
mkdir -p light
cp -r temp-light/light_build/* light/
rm -rf temp-light

echo "✅ Done!"
