from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

imp_search = (By.NAME, "q")

# driver.set_page_load_timeout(1)
driver.set_page_load_timeout(2)
start_time = time.time()
driver.get("http://google.com")
end_time = time.time() - start_time
print("Page Loading Time : {:.2f}".format(end_time))

driver.find_element(*imp_search).send_keys("test" + Keys.ENTER)
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.ID, ""))
# wait and return when element located


time.sleep(1)
driver.quit()
