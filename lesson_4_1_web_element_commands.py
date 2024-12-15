# ---------Web-elements Commands-----------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://python.org")
search_field = driver.find_element(By.ID, 'id-search-field') 
search_field.send_keys('test')
time.sleep(2)
search_field.clear()
search_field.send_keys('test')
go_button = driver.find_element(By.ID, 'submit')
print("="*100)
if go_button.is_enabled():
    print(go_button.text)
print(search_field.get_attribute("placeholder"))    
print("="*100)
go_button.click()
time.sleep(2)
driver.quit()
