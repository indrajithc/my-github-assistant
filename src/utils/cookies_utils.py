import json
import os
import time

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
    print('Loading cookies...')
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            cookies = json.load(file)

        print('Loading previous session...')
        for cookie in cookies:
            print(cookie)
            driver.add_cookie(cookie)
        time.sleep(1)
        driver.refresh()
        print('Previous session loaded')
    else:
        print('No cookies file found')

# Example usage:
# save_cookies(driver)
# load_cookies(driver)
