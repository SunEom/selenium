import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

INSTA_ID="USERNAME"
INSTA_PWD="PASSWORD"

browser = webdriver.Chrome(ChromeDriverManager().install())

main_hashtag = "정은지"

browser.get(f"https://www.instagram.com/explore/tags/{main_hashtag}/");

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "_2hvTZ")))

insta_id = browser.find_element_by_name("username");
insta_pwd = browser.find_element_by_name("password");

insta_id.send_keys(INSTA_ID)
insta_pwd.send_keys(INSTA_PWD)
insta_pwd.send_keys(Keys.ENTER)

time.sleep(5)
browser.find_element_by_class_name("yWX7d").click()
browser.find_element_by_class_name("HoLwm").click()

search_bar = browser.find_element_by_class_name("x3qfX")
search_bar.send_keys(f"#{main_hashtag}")

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))

hashtags = browser.find_elements_by_class_name("_2_M76")
results = [];
for hashtag in hashtags : 
    results.append({"title":  hashtag.find_element_by_class_name("Ap253").text, "number":  hashtag.find_element_by_class_name("Fy4o8").text.replace("게시물 ","")})

for result in results : 
    print(result)



time.sleep(5);
browser.quit()