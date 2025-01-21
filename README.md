Image Scraper and Dataset Generator
This project is a Python-based script for scraping images from Google Images and creating datasets for various purposes, such as machine learning, research, or data collection. The script includes features to filter out irrelevant images and augment collected data.

Features
Web Scraping: Automates image scraping from Google Images using Selenium.
Filtering: Skips irrelevant images based on dimensions, keywords, and content.
Dataset Preparation: Automatically downloads images into a structured directory.
Image Augmentation: (Optional) Enhances the dataset by applying transformations like resizing, rotation, and noise addition.
Table of Contents
Installation
Usage
Configuration
Limitations
Future Improvements
Installation
Prerequisites
Python: Ensure Python 3.7 or higher is installed.
Google Chrome: Install the latest version of Google Chrome.
ChromeDriver: Download ChromeDriver matching your Chrome version. Guide
Install Required Libraries
Run the following command to install dependencies:

bash
Copy
Edit
pip install selenium requests opencv-python imgaug
Usage
Clone the Repository: Clone this repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/image-scraper.git
cd image-scraper
Set Up ChromeDriver: Update the PATH variable in the script with the path to your chromedriver.exe:

python
Copy
Edit
PATH = "D:\\path\\to\\chromedriver.exe"
Run the Script: Execute the Python script:

bash
Copy
Edit
python scraper.py
Provide a Search Query: Modify the search_url variable in the script with your desired search query. For example:

python
Copy
Edit
search_url = "https://www.google.com/search?q=cats&tbm=isch"
Output: Images will be saved in an img directory in the project folder.

Configuration
Filtering
Minimum Dimensions: Filter out small images by updating the threshold:
python
Copy
Edit
if width < 50 or height < 50:
    # Skip images smaller than 50x50
Keyword Filtering: Avoid specific images (e.g., logos) by adding conditions:
python
Copy
Edit
if "logo" in src.lower() or "youtube" in src.lower():
    # Skip logos or irrelevant images
Image Augmentation
To augment images:

Install imgaug and use the augmentation snippet:
python
Copy
Edit
from imgaug import augmenters as iaa

augmenters = iaa.Sequential([
    iaa.Affine(rotate=(-15, 15)),
    iaa.Fliplr(0.5),
    iaa.Multiply((0.8, 1.2)),
    iaa.AdditiveGaussianNoise(scale=(10, 20))
])
Apply transformations to the scraped images to increase dataset diversity.
Limitations
Relevance: Scraped images depend on search engine accuracy and may include irrelevant results.
Rate Limits: Excessive scraping can trigger rate limits or captchas.
Diversity: Results are limited by the search engine's output.
Future Improvements
Multi-Source Support: Add functionality for scraping from additional sources (e.g., Bing Images, Reddit).
Advanced Filters: Implement AI-based filtering to remove irrelevant images automatically.
Captcha Handling: Integrate tools to bypass or resolve captchas.
Contributing
Contributions are welcome! If you find a bug or have an improvement idea, please fork this repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
For questions or suggestions:

Name: yahya2201129@gmail.com
GitHub: Yahya bawadekji
