from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)


driver.get("https://www.python.org")
time.sleep(2)
assert "Welcome to Python.org" in driver.title
driver.find_element(By.ID, "id-search-field").send_keys("bla bla bla ")
driver.find_element(By.ID, "submit").click()
assert "No results found." in driver.page_source
time.sleep(2)
