from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://uitestingplayground.com/home")
driver.maximize_window()
el = driver.find_element(By.XPATH, "//a[text()='Class Attribute']")
el.click()
time.sleep(1)
buttons = driver.find_elements(By.XPATH, "//h4[text()='Playground']/following-sibling::button")
for i in buttons:
    print(i.get_attribute("class"))
time.sleep(1)
driver.close()
