import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("message", [
    "Hello",
    "Selenium Automation",
    "12345"
])
def test_simple_form_submission(driver, base_url, message):
    driver.get(base_url + "simple-form-demo")

    driver.find_element(By.ID, "user-message").send_keys(message)
    driver.find_element(By.ID, "showInput").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    assert driver.title != ""


def test_checkbox_demo(driver, base_url):
    driver.get(base_url + "checkbox-demo")

    assert driver.title != ""


def test_dropdown_selection(driver, base_url):
    driver.get(base_url + "select-dropdown-demo")

    dropdown = Select(driver.find_element(By.ID, "select-demo"))
    dropdown.select_by_visible_text("Wednesday")

    assert dropdown.first_selected_option.text == "Wednesday"