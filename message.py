#WIP - Need refactor
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from redirect import redirect_to_main_page
import time

def send_messages_to_user(self,driver, username,message,delay):
    #Go to chat
    driver.find_element_by_xpath('//a[contains(@href, "/direct/inbox/")]').click()  
    #Go to user
    time.sleep(5)
    driver.find_element_by_xpath('//div[text()="'+ username + '"]').click()

    time.sleep(5)

    for i in range(delay):
        driver.find_element_by_xpath('//textarea[@placeholder="Envía un mensaje..."]').send_keys(message)
        driver.find_element_by_xpath('//button[text()="Enviar"]').click()
        if(i+1)%10==0:
            print("Mensaje #"+str(i+1))
    
    redirect_to_main_page(driver)