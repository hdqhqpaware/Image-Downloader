import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def download_images_from_webpage(url, output_dir="downloaded_images"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get the webpage content
    response = requests.get(url)
    response.raise_for_status()
    
    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all image tags
    img_tags = soup.find_all("img")
    print(f"Found {len(img_tags)} images.")
    
    for i, img in enumerate(img_tags, start=1):
        img_url = img.get("src")
        if not img_url:
            continue
        # Make image URL absolute
        img_url = urljoin(url, img_url)
        try:
            img_data = requests.get(img_url).content
            # Extract image filename
            parsed_url = urlparse(img_url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = f"image_{i}.jpg"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, "wb") as f:
                f.write(img_data)
            print(f"Downloaded: {img_url} -> {filepath}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

if __name__ == "__main__":
    webpage_url = input("Enter the webpage URL: ").strip()
    download_images_from_webpage(webpage_url)
