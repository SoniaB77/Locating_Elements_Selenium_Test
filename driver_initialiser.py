from selenium.webdriver import Chrome
import selenium
from webdriver_manager.chrome import ChromeDriverManager


def driver_finder():
    try:
        driver = Chrome()
    except selenium.common.exceptions.WebDriverException:
        driver = Chrome(ChromeDriverManager().install())
    finally:
        return driver