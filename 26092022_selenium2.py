from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "/home/halovivek/Downloads/Education"
driver = webdriver.Chrome(chrome_options = options, executable_path=r'/home/halovivek/Downloads/Education/')
driver.get('http://google.com/')
print("Chrome Browser Invoked successfully")
driver.quit()