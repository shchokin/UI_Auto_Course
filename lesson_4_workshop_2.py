from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://uitestingplayground.com/home") 
driver.maximize_window()
el = driver.find_element(By.XPATH, "//a[text()='Mouse Over']")
el.click()
time.sleep(2)
count = driver.find_element(By.ID, "clickCount")
for i in range(0, 5):
    btn_click_me = driver.find_element(By.XPATH, "//a[text()='Click me']")
    btn_click_me.click()
    time.sleep(2)

count = driver.find_element(By.ID, "clickCount")
print(count.text)
print(i + 1)
assert int(count.text) == (i + 1)
