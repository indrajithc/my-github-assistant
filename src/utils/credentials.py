import os
import getpass

class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def get_github_credentials():
    """
    Read GitHub username and password from config.yaml file.
    If not found, prompt user for password.
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
 