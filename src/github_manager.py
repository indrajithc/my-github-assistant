import os
import getpass  
from src.auth import login_github
from src.utils.credentials import get_github_credentials
 
def main_action(driver):

    # Get GitHub credentials
    github_credentials = get_github_credentials()
    
    # Login to GitHub
    login_github(driver, github_credentials)

 