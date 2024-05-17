from selenium.webdriver.common.by import By
from src.utils.common_utils import wait_until_element_present
from src.utils.common_utils import wait_until
from src.utils.cookies_utils import save_cookies


def check_logged_in(driver): 
    print("Checking if logged in...")
    try:
      profile_link =   "//*[@aria-label='Open user account menu']"
      element = driver.find_element("xpath",profile_link)
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
    driver.get('https://github.com')
    
        
    is_not_logged_in = driver.find_elements(By.LINK_TEXT, 'Sign in')
    
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
        
        profile_link =  "//*[@aria-label='Open user account menu']"
        
        try:
          if not check_logged_in(driver):
            raise Exception("Failed to log in to GitHub.")
          print("Successfully logged in to GitHub.")
        except:
          def callback_check_logged_in():
            return check_logged_in(driver)
          
          print("Failed to log in to GitHub.")
          wait_until(callback_check_logged_in, 360)
        
        if driver.find_elements("xpath", profile_link):
          print("Successfully logged in to GitHub.")
          save_cookies(driver)
          
        
