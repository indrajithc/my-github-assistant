from selenium.webdriver.common.by import By

def login_github(driver, credentials):
    """
    Log in to GitHub using the provided driver and credentials.
    """
    driver.get('https://github.com/login')

    username_input = driver.find_element(By.NAME, 'login')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(credentials.username)
    password_input.send_keys(credentials.password)
    password_input.submit()
