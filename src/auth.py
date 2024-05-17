from selenium.webdriver.common.by import By
from src.utils.common_utils import wait_until_element_present
from src.utils.common_utils import wait_until
from src.utils.cookies_utils import save_cookies
from src.utils.cookies_utils import load_cookies

from src.utils.constants import GITHUB_HOME_URL
from src.configurations.read import read_xpath
import time
import os


def check_logged_in(driver):
    print("Checking if logged in...")
    try:
        element = driver.find_element(
            By.XPATH, read_xpath("SESSION_USER_XPATH"))
        if element:
            print("Element found")
            return True
        else:
            raise Exception("Element not found")
    except:
        print("Element not found")
        return False


def login_github(driver, credentials):
    """
    Log in to GitHub using the provided driver and credentials.
    """
    driver.get(GITHUB_HOME_URL)

    print("============================== LOGIN ==============================")
    time.sleep(2)

    try:
        load_cookies(driver)
    except Exception as e:
        print(e)
        print("No cookies found")

    time.sleep(1)

    driver.get(GITHUB_HOME_URL)

    is_not_logged_in = driver.find_elements(By.LINK_TEXT, 'Sign in')

    print("is_not_logged_in: ", is_not_logged_in)

    if is_not_logged_in:
        sign_in_link = driver.find_element(By.LINK_TEXT, 'Sign in')
        sign_in_link.click()

        # Wait until element is present, visible, and interactable
        wait_until_element_present(driver, (By.NAME, 'login'))

        username_input = driver.find_element(By.NAME, 'login')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys(credentials.username)
        password_input.send_keys(credentials.password)
        password_input.submit()

        try:
            if not check_logged_in(driver):
                raise Exception("Failed to log in to GitHub.")
            print("Successfully logged in to GitHub.")
        except:
            def callback_check_logged_in():
                return check_logged_in(driver)

            print("Failed to log in to GitHub.")
            wait_until(callback_check_logged_in, 360)

    if driver.find_elements(By.XPATH, read_xpath("SESSION_USER_XPATH")):
        print("Successfully logged in to GitHub.")
        if os.getenv('PRESERVE_COOKIES'):
            save_cookies(driver)
