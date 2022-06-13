from selenium import webdriver

class Test_Firefox():
    def launch_firefox(self):
        #instantiate firefox
        driver = webdriver.Firefox(executable_path="D:\Project\AutomationBITM06\Drivers\geckodriver_0.31.0.exe")
        driver.get("http://localhost:3000/files/battlefield/react/react-hotel-reservation-system")
        #driver.quit()

firefox_obj=Test_Firefox()
firefox_obj.launch_firefox()