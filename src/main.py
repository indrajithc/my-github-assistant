import os
from src.auth import login_github
from src.utils.selenium_utils import get_selenium_driver
from src.github_manager import main_action
from dotenv import load_dotenv
from src.utils.constants import CACHE_PATH
from src.utils.configuration_utils import sync_static_configuration


def main():
    # Load environment variables from .env file
    load_dotenv()

    if not os.path.exists(CACHE_PATH):
        os.makedirs(CACHE_PATH)

    # Sync static configurations
    sync_static_configuration()

    # Get Selenium driver
    driver = get_selenium_driver()

    main_action(driver)

    # Add more functionality here


if __name__ == '__main__':
    main()
