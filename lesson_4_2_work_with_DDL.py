# ---------Work with DDL-----------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://amazon.com")
select_obj = Select(driver.find_element(By.ID, 'searchDropdownBox'))
select_obj.select_by_index(3)
time.sleep(2)
select_obj.select_by_visible_text('Computers')
# -----------or driver.find_element_by_id('searchDropdownBox').send_keys('Baby')
time.sleep(2)
select_obj.select_by_value('search-alias=digital-music')
time.sleep(2)
driver.close()
