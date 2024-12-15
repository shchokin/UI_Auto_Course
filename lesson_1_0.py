from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


browsers = ["Chrome", "Edge"]

# pip install --upgrade webdriver-manager
for browser in browsers:
    if browser == "Chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "Edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        print("\nCurrent browser is not supported")
        break
    driver.get("https://www.facebook.com")
    username = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "pass")
    submit = driver.find_element(By.NAME, "login")
    username.send_keys("artyomzp@gmail.com")
    password.send_keys("23otrby08fhntv85f")
    submit.click()
    time.sleep(5)
    assert "Facebook" in driver.title
    driver.quit()
