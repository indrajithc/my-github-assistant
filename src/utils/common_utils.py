from src.utils.constants import IMPLICIT_ELEMENT_WAIT_DELAY
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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