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

    def check_element():
        if wait_until_element_present(driver, (By.XPATH, read_xpath("SESSION_USER_XPATH"))):
            return True
        else:
            return False

    wait_until(check_element, 360)

    driver.find_element(By.XPATH, read_xpath("SESSION_USER_XPATH")).click()


def click_element_by_text(driver, text):
    """
    Click an element by text.
    """
    print(f"Clicking element by text: {text}")

    def check_element():
        if wait_until_element_present(driver, (By.LINK_TEXT, text)):
            return True
        else:
            return False

    wait_until(check_element, 360)

    element = driver.find_element(By.LINK_TEXT, text)
    element.click()


def open_user_profile(driver):
    """
    Open user profile.
    """
    print("Opening user profile...")

    open_user_account_menu(driver)

    click_element_by_text(driver, read_label("YOUR_PROFILE"))

    def check_element():
        if wait_until_element_present(driver, (By.XPATH, read_xpath("PERSON_XPATH"))):
            return True
        else:
            return False

    wait_until(check_element, 360)


def get_person_item(driver):
    """
    Get person item.
    """
    person_xpath = read_xpath("PERSON_XPATH")
    print(f"Getting person item: {person_xpath}")
    element = driver.find_element(By.XPATH, person_xpath)
    if element:
        print("Element person found")
    else:
        print("Element person not found")
    return element


def load_all_followers(driver):
    """
    Load all followers.
    """
    print("Loading all followers...")

    item_person = get_person_item(driver)

    if item_person:
        def check_element():
            if wait_until_element_present(driver, (By.PARTIAL_LINK_TEXT, read_label("FOLLOWER"))):
                return True
            else:
                return False

        wait_until(check_element, 360)

        element = item_person.find_element(
            By.PARTIAL_LINK_TEXT, read_label("FOLLOWER"))
        if element:
            print("Element found")
            element.click()
        else:
            print("Element not found")


def main_action(driver):

    # Get GitHub credentials
    github_credentials = get_github_credentials()

    # Login to GitHub
    login_github(driver, github_credentials)

    # Open user profile
    open_user_profile(driver)

    load_all_followers(driver)
