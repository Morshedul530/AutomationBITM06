from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Upload():
    def test_upload(self):
        file = 'C:\\Users\\morsh\\Desktop\\selenium_logo.png'
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My Info Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()
        time.sleep(2)

        # click Contact Details
        driver.find_element(By.LINK_TEXT, 'Contact Details').click()

        # Add Attachment
        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(1)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(1)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(1)

        select_file = driver.find_element(By.ID, 'ufile')
        select_file.send_keys(file)
        time.sleep(2)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('The image uploaded successfully')
        time.sleep(1)

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()

        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        time.sleep(2)

        driver.close()


test_obj = Upload()
test_obj.test_upload()