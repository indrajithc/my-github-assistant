from src.utils.constants import IMPLICIT_ELEMENT_WAIT_DELAY
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def wait_until(condition, timeout=IMPLICIT_ELEMENT_WAIT_DELAY, interval=0.5):
    """Wait until the condition is true or timeout."""
    end_time = time.time() + timeout
    while time.time() < end_time:
        if condition():
            return True
        time.sleep(interval)
    return False


def wait_until_element_present(driver, element):
    """Wait until the element is present in the DOM."""
    try:
        return WebDriverWait(driver, IMPLICIT_ELEMENT_WAIT_DELAY).until(EC.visibility_of_all_elements_located(element))
    except TimeoutException:
        print(f"Element {element} not found")
        return False


def read_json_file(path):
    data = {}
    try:
        if os.path.exists(path):
            with open(path, 'r') as file:
                data = json.load(file)
    except Exception as e:
        print(e)
        print("No data found")
    return data


def write_json_file(path, data):
    with open(path, 'w') as file:
        json.dump(data, file)
    print('New configurations saved successfully')
