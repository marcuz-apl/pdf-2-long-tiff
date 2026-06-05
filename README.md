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
from pathlib import Path

from pdf2image import convert_from_path
from PIL import Image


def pdf_to_long_tiff(pdf_path, output_tiff_path, dpi=200):
    print(f"Extracting PDF pages from: {pdf_path}")
    # Convert PDF pages to PIL Image objects
    pages = convert_from_path(pdf_path, dpi=dpi)

    if not pages:
        print("No pages found.")
        return

    # Calculate dimensions for the long stitched image
    total_width = max(page.width for page in pages)
    total_height = sum(page.height for page in pages)

    print(f"Stitching {len(pages)} pages into a {total_width}x{total_height} image...")
    # Create a blank canvas matching the total height
    long_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))

    # Paste pages sequentially from top to bottom
    current_y = 0
    for page in pages:
        long_image.paste(page, (0, current_y))
        current_y += page.height

    # Save the final stitched canvas as a TIFF image
    long_image.save(output_tiff_path, format='TIFF', compression='tiff_lzw')
    print(f"Success! Saved long image to: {output_tiff_path}")


def convert_input_folder(input_dir="./inputs", output_dir="./outputs", dpi=200):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(input_path.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in: {input_path}")
        return

    print(f"Found {len(pdf_files)} PDF file(s) in: {input_path}")
    for pdf_file in pdf_files:
        output_file = output_path / f"{pdf_file.stem}_long_image.tiff"
        pdf_to_long_tiff(pdf_file, output_file, dpi=dpi)


if __name__ == "__main__":
    convert_input_folder(dpi=200)
```

## Run the code
Put one or more PDF files in `./inputs`. Each PDF is converted to a separate TIFF in `./outputs` using the original PDF filename:

```text
inputs/sample.pdf       -> outputs/sample_long_image.tiff
inputs/report.pdf       -> outputs/report_long_image.tiff
```

```shell
## uv python
uv run main.py
## pure python
python main.py
```
