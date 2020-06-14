from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(self,driver,user, password):
        instagramlink = "https://www.instagram.com/"

        driver.get(instagramlink)

        driver.implicitly_wait(10) #Wait Time

        driver.find_element_by_name("username").send_keys(user)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath('//div[text()="Iniciar sesión"]').click()

        nowbutton = '//button[text()="Ahora no"]'

        for i in range(2):
            try:
                self.element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, nowbutton))
                )
            finally:
                driver.find_element_by_xpath(nowbutton).click()

        print("Ready to action !!!")