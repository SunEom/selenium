import time 
import os
from math import ceil
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

BROWSER_HEIGHT = 1056;

class ResponsiveTester :
    def __init__(self,urls):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.maximize_window()
        self.urls = urls;
        self.sizes = [ 480, 960, 1366, 1920]

    def screenshot(self,url):
        BROWSER_HEIGHT = 1056;
        self.browser.get(url)
        host_name = self.browser.execute_script("return window.location.hostname.replace('www.','').split('.')[0]")
        if not os.path.exists(f"screenshots/{host_name}"):
            os.makedirs(f"screenshots/{host_name}")
        for size in self.sizes : 
            self.browser.set_window_size(size,BROWSER_HEIGHT)
            self.browser.execute_script("window.scrollTo(0,0)")
            time.sleep(1)
            scroll_size = self.browser.execute_script("return document.body.scrollHeight")
            total_sections = ceil(scroll_size / BROWSER_HEIGHT)
            for section in range(total_sections+1):
                self.browser.execute_script(f"window.scrollTo(0,{(section) * BROWSER_HEIGHT})")
                self.browser.save_screenshot(f"screenshots/{host_name}/{size}x{section+1}.png")
                time.sleep(1)

    def start(self):
        for url in self.urls:
            self.screenshot(url)

tester = ResponsiveTester(["https://nomadcoders.co","https://github.com"])
tester.start()