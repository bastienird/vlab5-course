#!/usr/bin/env bash
set -e

which quarto >/dev/null 2>&1
if [ $? -ne 0 ]; then
curl -L https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.23/quarto-1.7.23-linux-amd64.deb --output /tmp/quarto.deb
dpkg -i /tmp/quarto.deb
fi

quarto render --to html
cp -r _site/* /app/repository
