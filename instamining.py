import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class InstagramHashtagMiner : 
    def __init__(self,keyword):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.keyword = keyword
        

    def start(self):
        self.login()
        self.search()
    
    def finish(self):
        time.sleep(5)
        self.browser.quit()

    def login(self):
        self.browser.get(f"https://www.instagram.com/");
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ")))

        insta_id = self.browser.find_element_by_name("username");
        insta_pwd = self.browser.find_element_by_name("password");

        insta_id.send_keys(input("What is your Username ? "))
        insta_pwd.send_keys(input("What is your Password ? "))
        insta_pwd.send_keys(Keys.ENTER)

        time.sleep(5)
        self.browser.find_element_by_class_name("yWX7d").click()
        self.browser.find_element_by_class_name("HoLwm").click()

    def search(self):
        search_bar = self.browser.find_element_by_class_name("x3qfX")
        search_bar.send_keys(f"#{self.keyword}")

        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))

        hashtags = self.browser.find_elements_by_class_name("_2_M76")
        results = [];
        for hashtag in hashtags : 
            results.append({"title":  hashtag.find_element_by_class_name("Ap253").text, "number":  hashtag.find_element_by_class_name("Fy4o8").text.replace("게시물 ","")})
        self.print_results(results)

    def print_results(self,results) :
        for result in results : 
            print(result)



dog_miner = InstagramHashtagMiner("강아지")
dog_miner.start()
dog_miner.finish()


