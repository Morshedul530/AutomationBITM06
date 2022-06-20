from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class Screenshot():
    def test_screenshot(self):

        # One Way
        base_url = 'https://jqueryui.com/droppable/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        file_name = "\\DragDrop"
        file_extension = '.png'
        file_destination_path = "D:\\Project\\AutomationBITM06\\ScreenshotFiles"

        try:
            driver.save_screenshot(file_destination_path + file_name + file_extension)
            print("Screenshot save to Directory --> :: " + file_destination_path)

        except:
            print("screenshot Capture Failed")

        # Another Way
        base_url = 'https://google.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)
        destination_file = "D:\\Project\\AutomationBITM06\\ScreenshotFiles\\google.png"

        try:
            driver.save_screenshot(destination_file)
            print("Screenshot save to Directory --> :: " + file_destination_path)

        except:
            print("screenshot Capture Failed")
            
test_obj = Screenshot()
test_obj.test_screenshot()

# Another Way
class Screenshot():
    def test_screenshot(self, url, file_name):
        # Another Way
        #url = 'https://jqueryui.com/droppable/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)
        #file_name = "DragDrop"
        file_extension = '.png'
        file_destination_path = "D:\\Project\\AutomationBITM06\\ScreenshotFiles\\"

        try:
            driver.save_screenshot(file_destination_path + file_name + file_extension)
            print("Screenshot save to Directory --> :: " + file_destination_path)

        except:
            print("screenshot Capture Failed")

        driver.close()


test_obj = Screenshot()
test_obj.test_screenshot('https://jqueryui.com/', 'New2')
