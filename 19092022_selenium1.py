import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=s, options=chrome_options)
"""
Above the basic setup to run the chrome browser
Below the project starts.
Find the locators and resetting the password
"""
name = "OVM"
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#time.sleep(5)
browser.maximize_window()
time.sleep(3)
"""
Implicit wait and explict wait 
"""
browser.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(3)
items_list = browser.find_elements(By.XPATH, "//div[@class='products']")
print(len(items_list))
count = len(items_list)
assert count > 0

