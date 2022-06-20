from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class BasicAuth():
    def test_auth(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        # Formula > Protocol(https)://username:password@url
        base_url = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'
        driver.get(base_url)
        time.sleep(5)


test_obj = BasicAuth()
test_obj.test_auth()