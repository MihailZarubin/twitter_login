import undetected_chromedriver

options = undetected_chromedriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-dev-shm-usage')

driver = undetected_chromedriver.Chrome(options=options)
driver.get("https://www.google.com/")
driver.close()
