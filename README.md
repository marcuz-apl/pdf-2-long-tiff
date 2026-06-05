# PDF-2-Long-Tiff

## Intro
A tool to convert PDF to long Tiff image file since I have no subcription to Acrobat DC.

## Pre-requisites
Have to go through a few steps:
```shell
## very essential Tools
apt install imagemagick poppler-utils
## Install uv if not done so
curl -LsSf https://astral.sh/uv/install.sh | sh
## Create the project folder
uv init pdf-2-long-tiff
cd pdf-2-long-tiff
```
Then open VS Code app and get auth from github:
```shell
## Launch VS COde
code .
## Authorizzation
gh auth login
## Create repo onto Github remotely
gh repo create https://github.com/marcuz-apl/pdf-2-long-tiff.git --public
## then first commit
git add .
git commit -m "pdf to long tiff"
git branch -M master
git remote add origin https://github.com/marcuz-apl/pdf-2-long-tiff.git
git push -u origin master
```

## Tech stack
- Python3
- Python module: pdf2image, pillow

Those can be installed by:
```shell
uv pip install -r ./requirements.txt
## If no uv env, then: pip install -r ./requirements.txt
```

## The main.py
```python

```

## Run the code
```shell
## uv python
uv run main.py
## pure python
python main.py
```
