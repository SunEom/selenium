import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InstagramKeywordScreenshooter:
    def __init__(self, keywords):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keywords = keywords
        

    def start(self):
        self.login()
        for keyword in self.keywords : 
            self.search(keyword);
            self.screenshot(keyword)

    def login(self):
        self.browser.get('https://www.instagram.com/')

        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "HmktE")))

        insta_username = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        insta_password = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

        insta_username.send_keys(input("What is your Username ? "))
        insta_password.send_keys(input("What is your Password ? "))
        insta_password.send_keys(Keys.ENTER)

        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cmbtv")))
        self.browser.find_element_by_class_name("yWX7d").click()
        self.browser.find_element_by_class_name("HoLwm").click()

    def search(self,keyword):
        search_bar = self.browser.find_element_by_class_name("x3qfX")
        search_bar.send_keys(f"#{keyword}")
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))
        self.browser.find_element_by_class_name("yCE8d").click()
        time.sleep(5)
    
    def is_dir(self, keyword):
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
            os.makedirs(f"screenshots/{keyword}")

        elif not os.path.exists(f"screenshots/{keyword}"):
            os.makedirs(f"screenshots/{keyword}")

    def screenshot(self,keyword):
        self.is_dir(keyword)
        imgs = self.browser.find_elements_by_class_name("eLAPa")
        for index,img in enumerate(imgs) :
            img.screenshot(f"screenshots/{keyword}/{keyword}x{index+1}.png")

    def finish(self):
        time.sleep(3);
        self.browser.quit()

screenshooter = InstagramKeywordScreenshooter(["고양이","강아지"])
screenshooter.start()
screenshooter.finish()




    

