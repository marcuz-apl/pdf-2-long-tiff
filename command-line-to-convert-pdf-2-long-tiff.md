# the Command line way to convert PDF to long tiff

## Install package
```shell
apt install imagemagick
```

## Give a shot
```shell
magick convert -density 200 sample.pdf -append -compress lzw ./outputs/long_image_2.tif
```
- `-density 200`: Controls the clarity/resolution (DPI) of the document.
- `-append`: Stacks pages top-to-bottom. (Use +append if you ever need side-by-side).
- `-compress lzw`: Ensures the file size stays optimized without sacrificing image quality.

## The End
