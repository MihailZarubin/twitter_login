import time
from selenium.webdriver.common.by import By


class Twitter:

    def __init__(self):
        self.driver = None
        self.domain_url = 'https://twitter.com/'
        self.home_page_url = 'https://twitter.com/home'
        self.login_page_url = 'https://twitter.com/login'

    def get_home_page_url(self):
        return self.home_page_url

    def get_login_page_url(self):
        return self.login_page_url

    def set_driver(self, driver):
        self.driver = driver

    def find_login_field(self):
        elements = self.wait_for_elements(By.XPATH,
                                          "//*[contains(text(), 'Phone')]/ancestor::*[3]//input")  # TODO: change to phone
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
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Next')]/ancestor::*[3]")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def find_enter_button(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Log in')]/ancestor::*[3]")
        if isinstance(elements, list):
            for element in elements:
                return element
        else:
            return None

    def type_twit(self, text):
        elements = self.wait_for_elements(By.CSS_SELECTOR, "div[role='textbox']")
        if isinstance(elements, list):
            for element in elements:
                element.send_keys(text)
                break

    def check_twit_input(self):
        elements = self.wait_for_elements(By.CSS_SELECTOR, "div[role='textbox']", 10)
        if isinstance(elements, list):
            return True
        else:
            return False

    def submit_twit(self):
        elements = self.wait_for_elements(By.XPATH, "//*[contains(text(), 'Tweet')]/ancestor::*[3]")
        if isinstance(elements, list):
            elements[2].click()

    def get_twits_on_page(self):
        elements = self.wait_for_elements(By.CSS_SELECTOR, "article[data-testid='tweet']")
        if isinstance(elements, list):
            return elements
        else:
            return None

    def get_likes_on_page(self):
        elements = self.wait_for_elements(By.CSS_SELECTOR, "article[data-testid='tweet'] div[aria-label*='Likes.']")
        if isinstance(elements, list):
            return elements
        else:
            return None

    def wait_for_elements(self, by, selector, repeat=90):

        for i in range(repeat):
            elements = self.driver.find_elements(by, selector)
            if elements:
                return elements
            else:
                time.sleep(0.3)
        return None
