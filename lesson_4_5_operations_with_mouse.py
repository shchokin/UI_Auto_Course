# -------------Operations with Mouse-----------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# ---------------------------------------------------------

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://python.org")
driver.maximize_window()

action = ActionChains(driver)
el = driver.find_element(By.XPATH, "//a[text()='Events']")
action.move_to_element(el).perform()
time.sleep(2)
el.click()
time.sleep(2)
driver.close()

