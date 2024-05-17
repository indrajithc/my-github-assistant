from src.auth import login_github
from src.utils.credentials import get_github_credentials
from src.utils.common_utils import wait_until_element_present
from selenium.webdriver.common.by import By
from src.utils.common_utils import wait_until
from src.configurations.read import read_label, read_xpath


def open_user_account_menu(driver):
    """
    Open user account menu.
    """
    print("Opening user account menu...")
    driver.find_element(By.XPATH, read_xpath("SESSION_USER_XPATH")).click()

    def check_element():
        if wait_until_element_present(driver, (By.XPATH, read_xpath("SESSION_USER_XPATH"))):
            return True
        else:
            return False

    wait_until(check_element, 360)


def click_element_by_text(driver, text):
    """
    Click an element by text.
    """
    print(f"Clicking element by text: {text}")
    element = driver.find_element(By.LINK_TEXT, text)
    element.click()

    def check_element():
        if wait_until_element_present(driver, (By.LINK_TEXT, text)):
            return True
        else:
            return False

    wait_until(check_element, 360)


def open_user_profile(driver):
    """
    Open user profile.
    """
    print("Opening user profile...")

    open_user_account_menu(driver)

    click_element_by_text(driver, read_label("YOUR_PROFILE"))


def main_action(driver):

    # Get GitHub credentials
    github_credentials = get_github_credentials()

    # Login to GitHub
    login_github(driver, github_credentials)

    # Open user profile
    open_user_profile(driver)
