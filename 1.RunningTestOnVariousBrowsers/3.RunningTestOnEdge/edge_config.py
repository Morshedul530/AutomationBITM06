from selenium import webdriver

class Test_Edge():
    def launch_edge(self):
        #instantiate firefox
        driver = webdriver.Edge(executable_path="D:\Project\AutomationBITM06\Drivers\msedgedriver_102.0.exe")


edge_obj=Test_Edge()
edge_obj.launch_edge()