# ---------------Working with 'Frames'--------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("https://easyhtmlcode.com/frames.html")
driver.maximize_window()
driver.switch_to.frame("main")
# Click on the 'Introduction' link
driver.find_element(By.XPATH, "//*[@id='bottomnav']//a").click()
driver.switch_to.default_content()
time.sleep(1)
driver.quit()
