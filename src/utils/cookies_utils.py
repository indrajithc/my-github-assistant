import json
import os

def save_cookies(driver, filename='cookies.json'):
    """
    Save browser cookies to a JSON file.
    """
    cookies = driver.get_cookies()

    with open(filename, 'w') as file:
        json.dump(cookies, file)
    print('New cookies saved successfully')

def load_cookies(driver, filename='cookies.json'):
    """
    Load cookies from a JSON file and add them to the browser session.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            cookies = json.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        print('Previous session loaded')
    else:
        print('No cookies file found')

# Example usage:
# save_cookies(driver)
# load_cookies(driver)
