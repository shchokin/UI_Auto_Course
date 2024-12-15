# ------------Operations with Windows-------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# -------------------------------------------------------

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://google.com")
driver.set_window_position(200, 300)
time.sleep(2)
driver.set_window_size(100, 100)
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.fullscreen_window()
time.sleep(2)
id = random.randint(0, 10000)
driver.save_screenshot(f'Screenshots/test{id}.png')
driver.close()
