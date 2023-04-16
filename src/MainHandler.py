import undetected_chromedriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from Twitter import Twitter
from Utils import Utils


class MainHandler:
    def __init__(self, user):
        self.user = user
        self.driver = None

    def init_browser(self):
        chrome_bin_path = Utils.get_settings_from_json()['chrome_bin_path']  # TODO: change
        chrome_user_dir = Utils.get_settings_from_json()['chrome_user_dir']  # TODO: change

        options = undetected_chromedriver.ChromeOptions()
        options.binary_location = chrome_bin_path
        options.add_argument('--user-data-dir=' + chrome_user_dir)

        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument(f"--window-size={Utils.get_random_width()},{Utils.get_random_height()}")
        options.add_argument(f"--user-agent={Utils.get_random_user_agent()}")

        driver = undetected_chromedriver.Chrome(options=options)
        self.driver = driver

    def login(self):
        self.driver.get('https://twitter.com/login')
        # time.sleep(10)  # wait for the page to load
        twitter = Twitter(self.driver)

        # fill email
        login_field_element = twitter.find_login_field()
        login_field_element.send_keys(self.user['email'])

        time.sleep(1)  # TODO: remove

        # click continue button
        continue_button_element = twitter.find_continue_button()
        continue_button_element.click()

        time.sleep(1)  # TODO: remove

        # fill password
        password_field = twitter.find_password_field()
        password_field.send_keys(self.user['password'])

        time.sleep(1)  # TODO: remove

        # click enter button
        enter_button_element = twitter.find_enter_button()
        enter_button_element.click()

        time.sleep(5)  # TODO: remove

    def clear_browser_cache(self):
        tabs_count = 1
        self.driver.get('chrome://settings/clearBrowserData')
        actions = ActionChains(self.driver)

        for i in range(tabs_count):
            actions.send_keys(Keys.TAB).perform()
            time.sleep(1)  # TODO: make less
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)  # TODO: make less

    def close_browser(self):
        self.driver.quit()
