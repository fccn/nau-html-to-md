# Conversion of Confluence export to Markdown

This repository has a script that allows to convert HTML to Markdown.

It allows to convert a specific single file or to multiple files at once.

Package: https://pypi.org/project/markdownify/
Dependency: https://github.com/matthewwithanm/python-markdownify

## Installation

You should use a virtual environment.

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage examples
To export a single html file to the stdout:
```bash
python python md.py confluence-export/index.html
```

To export a single html file to a md file:
```bash
python python md.py --in examples/index.html --out output/index.md
```

To export all html files from a folder:
```bash
find path-to/confluence/export/project/ -name *.html -exec python md.py --in {} --out output/{}.md \;
```
