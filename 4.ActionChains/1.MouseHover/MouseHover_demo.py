from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver import ActionChains


class MouseHovering():
    def test_mouseHover(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Login
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()
        time.sleep(2)

        # Recruitment
        recruitment = driver.find_element(By.XPATH, '//*[@id="menu_recruitment_viewRecruitmentModule"]/b')

        try:
            actions = ActionChains(driver)
            actions.move_to_element(recruitment).perform()
            time.sleep(2)

            Candidates = driver.find_element(By.LINK_TEXT, 'Candidates')
            Candidates.click()
            time.sleep(2)

        except:
            print('Mouse Hover Action Failed')

        driver.close()


test_obj = MouseHovering()
test_obj.test_mouseHover()
