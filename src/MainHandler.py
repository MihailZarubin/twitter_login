import time
import hashlib
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Twitter import Twitter
from Utils import Utils
from OpenAIService import OpenAIService


class MainHandler:

    def __init__(self):
        self.user = None
        self.driver = None
        self.twitter = Twitter()
        self.settings = Utils.get_settings_from_json()
        self.open_ai_service = OpenAIService()

    def set_user(self, user):
        self.user = user
        self.open_ai_service.set_user(user)  # TODO: not good

    def init_browser(self):
        chrome_bin_path = self.settings['chrome_bin_path']
        chrome_user_dir = self.settings['chrome_user_dir_prefix'] + 'User Data Twitter ' + str(self.user['id'])

        chrome_options = ChromeOptions()
        chrome_options.binary_location = chrome_bin_path
        chrome_options.add_argument('--user-data-dir=' + chrome_user_dir)
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument(f"--window-size={Utils.get_random_width()},{Utils.get_random_height()}")
        chrome_options.add_argument(f"--user-agent={Utils.get_random_user_agent()}")

        driver = webdriver.Remote(
            command_executor=f'http://localhost:786/wd/hub',
            desired_capabilities=chrome_options.to_capabilities()
        )
        self.driver = driver
        self.twitter.set_driver(driver)

    def login(self):
        self.driver.get(self.twitter.login_page_url)

        # login input
        login_field_element = self.twitter.find_login_field()
        if login_field_element:
            login_field_element.send_keys(self.user['email'])  # fill email

            # continue button
            continue_button_element = self.twitter.find_continue_button()  # click continue button
            if continue_button_element:
                continue_button_element.click()

                # password input
                password_field = self.twitter.find_password_field()
                if password_field:
                    password_field.send_keys(self.user['password'])  # fill password

                    # enter button
                    enter_button_element = self.twitter.find_enter_button()
                    if enter_button_element:
                        enter_button_element.click()  # click enter button

    def create_twit(self, text):
        if self.driver.current_url != self.twitter.home_page_url:
            self.driver.get(self.twitter.home_page_url)

        self.twitter.type_twit(text)
        self.twitter.submit_twit()

    def create_twit_ai(self, prompt):
        if self.driver.current_url != self.twitter.home_page_url:
            self.driver.get(self.twitter.home_page_url)

        text = self.open_ai_service.generate_twit_text(prompt)
        self.twitter.type_twit(text)
        self.twitter.submit_twit()

    def check_log_in(self):
        if self.driver.current_url != self.twitter.home_page_url:
            self.driver.get(self.twitter.home_page_url)

        res = self.twitter.check_twit_input()
        if not res:
            print('>>> User with id: ' + str(self.user['id']) + ' is not logged in. Skipping it.')
        else:
            print('>>> User with id: ' + str(self.user['id']) + ' user is successfully logged in.')
        return res

    def like_user_twits(self, username, max_likes_count=10, question_to_ai=''):
        self.driver.get(self.twitter.domain_url + username)
        liked_elements = {}
        current_likes_count = 0

        while True:
            actions = ActionChains(self.driver)
            likes_elements = self.twitter.get_likes_on_page()

            if likes_elements:
                for like_element in likes_elements:

                    if current_likes_count >= max_likes_count:
                        break

                    try:
                        js_to_get_parent = "return arguments[0].parentNode.parentNode.parentNode.parentNode;"
                        twit_text = self.driver.execute_script(js_to_get_parent, like_element).text
                        actions.move_to_element(like_element).perform()

                        if question_to_ai != '':
                            prompt_options = 'Write only Yes or No.'
                            prompt = question_to_ai + ' ' + prompt_options + ' ' + twit_text
                            ai_response = self.open_ai_service.get_response(prompt)
                            print('>>> Q: ' + question_to_ai + ' | ' + 'R: ' + ai_response)
                            # like twit only if AI response it Yes
                            if ai_response.find('Yes'):
                                like_element.click()
                        else:
                            like_element.click()

                        time.sleep(0.5)
                        self.driver.execute_script("arguments[0].remove()", like_element)
                        current_likes_count = current_likes_count + 1
                    except:
                        continue

            if current_likes_count >= max_likes_count:
                break

    def clear_browser_cache(self):
        tabs_count = 1
        self.driver.get('chrome://settings/clearBrowserData')
        actions = ActionChains(self.driver)

        for i in range(tabs_count):
            actions.send_keys(Keys.TAB).perform()
            time.sleep(0.5)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)

    def close_browser(self):
        self.driver.quit()
