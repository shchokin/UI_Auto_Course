# -------------Operations with Windows: Switch To------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ---------------------------------------------------------

s = Service(ChromeDriverManager(path=r".\\Drivers").install())
driver = webdriver.Chrome(service=s)

driver.get("http://amazon.com")
wind1 = driver.window_handles[0]
# ---------------------------------------------------------
driver.execute_script('window.open('');')
wind2 = driver.window_handles[1]
driver.switch_to.window(wind2)    # or driver.switch_to_window(wind2) --> can not working!
driver.get("http://python.org")

# --------------------------------------------------------

time.sleep(2)
for wind in driver.window_handles:
    driver.switch_to.window(wind)
    print(driver.title)
    print(driver.current_url)

# --------------------------------------------------------
time.sleep(2)
driver.quit()
