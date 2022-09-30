import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
s = Service(GeckoDriverManager().install())
#s = Service(ChromeDriverManager().install())
firefox_options = Options()
"""
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
"""
browser = webdriver.Firefox(service=s, options=firefox_options)
# browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
browser.implicitly_wait(5)

"""
Going to use drag and drop 
get the details from the mouse hover details
Action is the class which helps to perform
at the end of the action you need to write perform to execute the things.

"""
browser.get("https://www.rahulshettyacademy.com/AutomationPractice")
print(browser.title)