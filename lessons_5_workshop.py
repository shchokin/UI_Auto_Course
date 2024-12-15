# ---------------Work Shop--------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

lnk_2017 = (By.XPATH, "//*[@id='BlogArchive1_ArchiveList']//a[text()=2017]")
lnk_google = (By.XPATH, "//*[@id='post-body-6170641642826198246']/a[@href='//www.google.com']")


def test():
    s = Service(ChromeDriverManager(path=r".\\Drivers").install())
    driver = webdriver.Chrome(service=s)

    driver.get("https://seleniumpractise.blogspot.com/")
    driver.maximize_window()
    driver.set_page_load_timeout(10)

    try:
        wait = WebDriverWait(driver, 10)
        element = wait.until(
            EC.presence_of_element_located(lnk_2017))
        element.click()
        element = wait.until(
            EC.presence_of_element_located(lnk_google))
        element.click()
        wind2 = driver.window_handles[1]
        driver.switch_to.window(wind2)
        print(driver.current_url)
        driver.close()
        time.sleep(1)
    finally:
        driver.quit()


if __name__ == "__main__":
    test()


