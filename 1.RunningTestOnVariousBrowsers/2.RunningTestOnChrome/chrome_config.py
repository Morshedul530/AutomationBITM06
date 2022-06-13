from selenium import webdriver

class Test_Chrome():
    def launch_chrome(self):
        #instantiate firefox
        driver = webdriver.Chrome(executable_path="D:\\Project\\AutomationBITM06\\Drivers\\chromedriver_102.0.exe")
        driver.get("http://localhost:3000/files/battlefield/react/react-hotel-reservation-system")


chrome_obj=Test_Chrome()
chrome_obj.launch_chrome()