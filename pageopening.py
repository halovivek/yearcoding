from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#browser = webdriver.Firefox()
browser.get('https://loosupaya.blogspot.com/')
browser.maximize_window()
print(browser.title)
time.sleep(10)
#browser.quit()