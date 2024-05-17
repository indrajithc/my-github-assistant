import os
import getpass  
from src.auth import login_github
from src.utils.selenium_utils import get_selenium_driver
from src.github_manager import main_action
from dotenv import load_dotenv 

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get Selenium driver
    driver = get_selenium_driver()

    main_action(driver)

    # Add more functionality here

if __name__ == '__main__':
    main()
