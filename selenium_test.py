from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

try:
    driver.get("https://www.google.com")
    driver.maximize_window()

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium jobs")
    search_box.submit()

    time.sleep(10)   # 10 seconds browser open থাকবে

finally:
    driver.quit()