from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        
import time
from redirect import redirect_to_main_page

def likes_posts_by_hashtag(self, driver, hashtag, delay):
        driver.implicitly_wait(2)
        
        searchinput = '//input[@placeholder="Busca"]'
        searchhashtag = str('//span[text()="'+ hashtag + '"]')
        firstpostclass = "//div[@class='_9AhH0']"

        heartpost ='//div[@class="_9AhH0"]'
        nextbutton = '//a[text()="Siguiente"]'

        liked = '//*[local-name()="svg" and @aria-label="Ya no me gusta"]'
        empty = '//span[@class="fr66n"] | //span[@class="FY9nT fr66n"]'
        
        driver.find_element_by_xpath(searchinput).send_keys(hashtag)

        #Search Hashtag
        try:
            self.element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, searchhashtag))
                )
        finally:
            driver.find_element_by_xpath(searchhashtag).click()

        time.sleep(3)
        #Enter to the first post
        firstpost = driver.find_element_by_xpath(firstpostclass)
        webdriver.ActionChains(driver).move_to_element(firstpost).click(firstpost).perform()

        likeimage = driver.find_element_by_xpath(empty)

        for i in range(delay):
            try:
                driver.find_element_by_xpath(liked) #Find liked post
                driver.find_element_by_xpath(nextbutton).click()

            except NoSuchElementException:
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, heartpost))
                    )
                
                likeimage = driver.find_element_by_xpath(empty)

                webdriver.ActionChains(driver).click(likeimage).perform()
                driver.find_element_by_xpath(nextbutton).click()
            if(i+1)%10==0:
                print("Post counter #"+str(i+1))

        redirect_to_main_page(driver)
