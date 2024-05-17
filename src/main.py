import os
import getpass
from src.auth import login_github
from src.utils.selenium_utils import get_selenium_driver

class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def get_github_credentials():
    """
    Read GitHub username from environment variable and prompt user for password.
    """
    username = os.getenv('GITHUB_USERNAME')
    password = os.getenv('GITHUB_PASSWORD')
    
    if not username or not password:
        print("GitHub username or password not found in environment variables.")

    if not username:
        username = input('Enter your GitHub username: ')

    if not password:
        password = getpass.getpass(prompt='Enter your GitHub password: ')
    
    return Credentials(username, password)

def main():
    # Get GitHub credentials
    github_credentials = get_github_credentials()
    
    # Get Selenium driver
    driver = get_selenium_driver()
    
    # Login to GitHub
    login_github(driver, github_credentials)

    # Add more functionality here

if __name__ == '__main__':
    main()
