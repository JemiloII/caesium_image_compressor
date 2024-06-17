# Caesium Image Compressor

A Python package for programmatically compressing images using the Caesium CLI.

## Installation
```bash
pip install caesium_image_compressor
```

## Optional Download
This step might be required if the Caesium CLI is not downloaded on pip install.
```bash
python -m caesium.downloader
```

## Usage
```python
from caesium import compress_image

# Compress an image
compress_image('path/to/image.jpg')

# Compress an image and save it to a different location
compress_image('path/to/image.jpg', 'path/to/compressed_image.jpg')

# Compress an image with a specific quality
compress_image('path/to/image.jpg', quality=50)

# Compress an image and drop the metadata
compress_image('path/to/image.jpg', exif=False)

# Compress an image and keep lossless
compress_image('path/to/image.jpg', lossless=True)

# Compress an image and show verbose logging
compress_image('path/to/image.jpg', verbose=True)
```

## Defaults
```python
def compress_image(
    image_path: str,
    output_path: str = None,
    quality: int = 75,
    exif: bool = True,
    lossless: bool = False,
    verbose: bool = False,
) -> None:
    ...

```

## License
Apache 2.0

## Author
[Brian Jemilo II](https://github.com/jemiloii)

## TODO
Return the compressed image as:
- [ ] cv2 image
- [ ] PIL Image
- [ ] numpy array
- [ ] base64 string
