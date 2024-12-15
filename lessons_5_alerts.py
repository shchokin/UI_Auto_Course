# ---------------Working with 'Alerts'--------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "alertbtn")))
    element.click()
    popupwind = driver.switch_to.alert
    time.sleep(1)
    print(popupwind.text)
    popupwind.accept()

finally:
    driver.quit()


