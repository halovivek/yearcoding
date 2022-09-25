import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
browser = webdriver.Chrome(service=s, options=chrome_options)
#browser = webdriver.Chrome(options=Options)
browser.implicitly_wait(5)

"""
Going to use drag and drop 
get the details from the mouse hover details

"""
browser.get("https://www.rahulshettyacademy.com/AutomationPractice")
browser.maximize_window()
print(browser.title)
#//a[normalize-space()='Top']
#//button[@id='mousehover']
#action = ActionChains(browser)
