from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.binary_location = "/home/halovivek/Downloads/Education"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

"""
The browser will be started.
"""
browser = webdriver.Chrome(executable_path="/home/halovivek/Downloads/Education/")
#browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
browser.get("https://rahulshettyacademy.com")
print(browser.title)
browser.get("https://rahulshettyacademy.com/angularpractice/")
print(browser.title)