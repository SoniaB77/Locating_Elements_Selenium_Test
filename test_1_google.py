from driver_initialiser import driver_finder
import time
from selenium.webdriver.common.keys import Keys

driver = driver_finder()

driver.get("https://www.google.com")
driver.maximize_window()
time.sleep(5)

agree = driver.find_element_by_id("L2AGLb").click()

search_box = driver.find_element_by_name("q").send_keys("Selenium")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()
