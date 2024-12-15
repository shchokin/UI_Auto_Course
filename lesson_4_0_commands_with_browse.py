# ---------Commands with browser-----------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://python.org") 
time.sleep(1)
driver.back()
time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
print("="*100)
print(driver.title)
print(driver.current_url)
print("="*100)
time.sleep(1)
driver.quit()
