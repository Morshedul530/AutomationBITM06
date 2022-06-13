from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chorome():
    def chrome_launch(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://google.com")
        driver.close()


test_obj = Chorome()
test_obj.chrome_launch()
