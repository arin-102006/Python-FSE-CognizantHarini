from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

driver.find_element(By.ID, "user-message").send_keys("Hello Selenium")
driver.find_element(By.ID, "showInput").click()

time.sleep(3)

print(driver.page_source)

driver.quit()