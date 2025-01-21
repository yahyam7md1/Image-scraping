from selenium import webdriver
import requests
import io
from selenium.webdriver.chrome.service import Service
from PIL import Image
import base64
import time
from selenium.webdriver.common.by import By



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
    search_url = "https://www.google.com/search?q=cat&tbm=isch"
    wd.get(search_url)

    image_urls = set()
    while len(image_urls) < max_images:
        scroll_down(wd)

        thumbnails = wd.find_elements(By.CLASS_NAME, "YQ4gaf")
        for img in thumbnails[len(image_urls): max_images]:
            try:
                img.click()
                time.sleep(delay)
            except:
                continue
            images = wd.find_elements(By.CLASS_NAME, "H8Rx8c")
            for image in images:
                if image.get_attribute("src") and "http" in image.get_attribute("src"):
                    image_urls.add(image.get_attribute("src"))
                    print("we found the image")
    return image_urls                



def download_image(base64_data, file_name):
    # Extract the Base64-encoded part of the data (after "base64,")
    if base64_data.startswith("data:image"):
        base64_data = base64_data.split(",")[1]

    # Decode the Base64 string into binary data
    image_data = base64.b64decode(base64_data)
    image_file = io.BytesIO(image_data)

    # Open the image using PIL and save it
    image = Image.open(image_file)
    image.save(file_name, "JPEG")
    print("Success: Image saved as", file_name)


urls = image_urls = get_images_from_google(wd, 2, 10)

    
