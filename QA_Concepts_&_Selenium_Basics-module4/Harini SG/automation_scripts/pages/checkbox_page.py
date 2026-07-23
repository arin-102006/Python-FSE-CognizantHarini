from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxPage(BasePage):

    def check_option(self, index=1):
        self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[index-1].click()

    def uncheck_option(self, index=1):
        self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[index-1].click()

    def is_option_checked(self, index=1):
        return self.driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[index-1].is_selected()