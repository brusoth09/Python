from datetime import datetime
from bs4 import BeautifulSoup
from security import safe_requests

if __name__ == "__main__":
    url = input("Enter image url: ").strip()
    print(f"Downloading image from {url} ...")
    soup = BeautifulSoup(safe_requests.get(url).content, "html.parser")
    # The image URL is in the content field of the first meta tag with property og:image
    image_url = soup.find("meta", {"property": "og:image"})["content"]
    image_data = safe_requests.get(image_url).content
    file_name = f"{datetime.now():%Y-%m-%d_%H:%M:%S}.jpg"
    with open(file_name, "wb") as fp:
        fp.write(image_data)
    print(f"Done. Image saved to disk as {file_name}.")
