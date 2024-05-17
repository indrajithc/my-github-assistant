from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def get_selenium_driver():
    """
    Get a Selenium driver instance.
    """
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")

    # Add logic to choose the appropriate driver (e.g., Chrome, Firefox, etc.) here
    # For now, let's use Chrome driver as an example
    driver = webdriver.Chrome(options=chrome_options)
    return driver