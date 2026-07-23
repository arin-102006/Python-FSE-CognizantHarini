from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.implicitly_wait(10)

# Open Selenium Playground
driver.get("https://www.lambdatest.com/selenium-playground/")
print("Title:", driver.title)

# Open Simple Form Demo
driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
assert "simple-form-demo" in driver.current_url
print("URL Verified")

# Go back
driver.back()

# Open Google in a new tab
driver.execute_script("window.open('https://www.google.com');")

# Switch to new tab
driver.switch_to.window(driver.window_handles[1])
print("Google Title:", driver.title)

# Switch back
driver.switch_to.window(driver.window_handles[0])

# Screenshot
driver.save_screenshot("playground_screenshot.png")
print("Screenshot Saved")

# Window size
print("Current Size:", driver.get_window_size())

driver.set_window_size(1280, 800)
print("New Size:", driver.get_window_size())

driver.quit()