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
        twitter = Twitter(self.driver)

        # login input
        login_field_element = twitter.find_login_field()
        if login_field_element:
            time.sleep(1)  # TODO: remove
            login_field_element.send_keys(self.user['email'])  # fill email

            # continue button
            continue_button_element = twitter.find_continue_button()  # click continue button
            if continue_button_element:
                time.sleep(1)  # TODO: remove
                continue_button_element.click()

                # password input
                password_field = twitter.find_password_field()
                if password_field:
                    time.sleep(1)  # TODO: remove
                    password_field.send_keys(self.user['password'])  # fill password

                    # enter button
                    enter_button_element = twitter.find_enter_button()
                    if enter_button_element:
                        time.sleep(1)  # TODO: remove
                        enter_button_element.click() # click enter button
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
