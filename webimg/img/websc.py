from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import base64
import io
import os
import time
import requests

# Provide the path to your ChromeDriver
PATH = "D:\\webimg\\chromedriver.exe"

# Use the Service object to specify the ChromeDriver executable
service = Service(PATH)

# Initialize the WebDriver with the Service object
wd = webdriver.Chrome(service=service)


def get_images_from_google(wd, delay, max_images):
    def scroll_down(wd):
        """Scrolls down the page to load more images."""
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)

    # Open Google Images search
    search_url = "https://www.google.com/search?q=cat&udm=2"
    wd.get(search_url)

    image_urls = set()
    image_count = 0
    results_start = 0

    while image_count < max_images:
        scroll_down(wd)

        # Find all thumbnail elements
        thumbnails = wd.find_elements(By.CLASS_NAME, "mNsIhb")  # Adjusted to match the correct thumbnail class

        for img in thumbnails[results_start:]:
            try:
                img.click()  # Click to load full-size image
                time.sleep(delay)

                # Find full-size images
                full_images = wd.find_elements(By.CLASS_NAME, "YQ4gaf")  # Adjusted to match full-size image class
                for image in full_images:
                    src = image.get_attribute("src")

                    # Get image dimensions
                    width = image.get_attribute("width")
                    height = image.get_attribute("height")

                    # Filter: Skip images smaller than 200x200 pixels
                    if int(width) < 50 or int(height) < 50:
                        print(f"Skipped image due to small size: {width}x{height}")
                        continue

                    # Check if the src is a valid URL
                    if src and "http" in src:
                        if src not in image_urls:  # Avoid duplicates
                            image_urls.add(src)
                            image_count += 1
                            print(f"Found {len(image_urls)}: {src}")

                            # Download the image immediately
                            download_image("img", src, f"image_{image_count}.jpg")

                        if len(image_urls) >= max_images:
                            break

            except Exception as e:
                print(f"Error: {e}")
                continue

        # Update results_start to avoid reprocessing thumbnails
        results_start = len(thumbnails)

    return image_urls


def download_image(path, url, file_name):
    """Downloads an image from a URL or decodes Base64 data and saves it to the specified path."""
    try:
        os.makedirs(path, exist_ok=True)  # Ensure the directory exists

        if url.startswith("data:image"):  # Handle Base64-encoded images
            base64_data = url.split(",")[1]
            image_data = base64.b64decode(base64_data)
            file_path = os.path.join(path, file_name)
            with open(file_path, "wb") as f:
                f.write(image_data)
            print(f"Success: Base64 image saved as {file_path}")
        else:  # Handle regular HTTP/HTTPS images
            response = requests.get(url, stream=True)
            response.raise_for_status()
            file_path = os.path.join(path, file_name)
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Success: Image saved as {file_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")


# Main script
delay = 2
max_images = 100
save_path = "img"

# Get image URLs
urls = get_images_from_google(wd, delay, max_images)

# Close the WebDriver
wd.quit()
