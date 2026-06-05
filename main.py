import os
from pdf2image import convert_from_path
from PIL import Image

def pdf_to_long_tiff(pdf_path, output_tiff_path, dpi=200):
    print("Extracting PDF pages...")
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


if __name__ == "__main__":
    pdf_to_long_tiff("./inputs/sample.pdf", "./outputs/sample_long_image.tiff", dpi=200)
