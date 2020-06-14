from selenium import webdriver
#Methods
from login import login
from hashtag import likes_posts_by_hashtag
from message import send_messages_to_user

#Globals

PATH = "C:\Program Files (x86)\Bot\chromedriver.exe"
initdriver = webdriver.Chrome(PATH)

class Bot:
    def __init__(self,user, password): 
        global initdriver
        return login(self, initdriver, user, password)
    
    def send_messages_to_user(self, username, message, quantity):
        global initdriver
        send_messages_to_user(self, initdriver, username, message, quantity)
        return 

    def likes_posts_by_hashtag(self, hashtag, delay):
        global initdriver
        return likes_posts_by_hashtag(self, initdriver, hashtag, delay)

    def exit(self):
        global driver

        driver.quit()
        print("Bye Bye")
        exit(0)

passw = "Insert Password"
user='Insert User'

bot = Bot(user, passw)