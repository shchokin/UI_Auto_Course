from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://uitestingplayground.com/home")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Verify Text']").click()
time.sleep(2)
txt_playground = driver.find_element(By.XPATH, "//div[@class='bg-primary']/span")
print(txt_playground.text)
