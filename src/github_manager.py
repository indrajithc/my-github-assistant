from src.auth import login_github
from src.utils.credentials import get_github_credentials
from src.utils.common_utils import wait_until_element_present
from src.utils.constants import SESSION_USER_XPATH
from selenium.webdriver.common.by import By
from src.utils.common_utils import wait_until



def open_user_account_menu(driver):
    """
    Open user account menu.
    """
    print("Opening user account menu...")
    driver.find_element(By.XPATH, SESSION_USER_XPATH).click()
    
    def check_element():
        if wait_until_element_present(driver, (By.XPATH,SESSION_USER_XPATH)):
            return True
        else:
            return False

    wait_until(check_element, 360)
            
    
 
def main_action(driver):

    # Get GitHub credentials
    github_credentials = get_github_credentials()
    
    # Login to GitHub
    login_github(driver, github_credentials)
    
    # Open user account menu
    open_user_account_menu(driver)
    
    

 