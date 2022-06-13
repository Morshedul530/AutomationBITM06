from selenium import webdriver
#from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
#import time


#class Firefox():
#def firefox_launch(self):
#driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
driver.get("https://google.com")
#time.sleep(2)
#driver.close()
#driver.quit()

#est_obj = Firefox()
#test_obj.firefox_launch()

