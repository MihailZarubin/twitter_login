from selenium.webdriver.common.by import By
import time


class Twitter:
    def __init__(self, driver):
        self.driver = driver

    def find_login_field(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'телефон')]/ancestor::*[3]//input")  # TODO: change to phone
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def find_password_field(self):
        elements = self.wait_for_elements(By.XPATH, "//input[@autocomplete='current-password']")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def find_continue_button(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Далее')]/ancestor::*[3]")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def find_enter_button(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Войти')]/ancestor::*[3]")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def type_tweet(self):
        elements = self.wait_for_elements(By.CSS_SELECTOR, "div[role='textbox']")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def click_button(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Tweet')]/ancestor::*[3]")
        if isinstance(elements, list):
            return elements
        else:
            return None

    def wait_for_elements(self, by, selector):

        # wait max ~30 sec for element to appear
        for i in range(90):
            elements = self.driver.find_elements(by, selector)
            if elements:
                return elements
            else:
                time.sleep(0.3)
        return None
