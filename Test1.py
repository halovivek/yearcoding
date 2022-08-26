import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

s = Service('/home/halovivek/Documents/Automation/selenium_driver/chromedriver.exe')

driver.maximize_window()

driver.get("https://www.google.com")
time.sleep(5)
print(driver.title)
