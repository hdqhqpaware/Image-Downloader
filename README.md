# Image Downloader

This Python script downloads all images from a given webpage.

## Features

- Parses a webpage and finds all image tags (`<img>`).
- Downloads images to a local folder.
- Handles both absolute and relative image URLs.

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:
```bash
pip install requests beautifulsoup4
```

## Usage

1. Save the script as `download_images.py`.
2. Run the script:
   ```bash
   python download_images.py
   ```
3. Enter the URL of the target webpage when prompted.
4. All images will be downloaded into the `downloaded_images` folder.

## Example

```bash
$ python download_images.py
Enter the webpage URL: https://example.com
Found 5 images.
Downloaded: https://example.com/img/logo.png -> downloaded_images/logo.png
...
```

## License

MIT
