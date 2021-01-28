import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

KEYWORD="아이유"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.instagram.com/')

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "HmktE")))

insta_username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
insta_password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

insta_username.send_keys(input("What is your Username"))
insta_password.send_keys(input("What is your Password"))
insta_password.send_keys(Keys.ENTER)

WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "cmbtv")))
browser.find_element_by_class_name("yWX7d").click()
browser.find_element_by_class_name("HoLwm").click()

search_bar = browser.find_element_by_class_name("x3qfX")
search_bar.send_keys(f"#{KEYWORD}")
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))
browser.find_element_by_class_name("yCE8d").click()

time.sleep(5)
imgs = browser.find_elements_by_class_name("eLAPa")

for index,img in enumerate(imgs) :
    img.screenshot(f"screenshots/{KEYWORD}x{index}.png")
    

time.sleep(3);
browser.quit()