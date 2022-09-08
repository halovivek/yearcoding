from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_object = Service("C:\Drivers\chromedriver.exe")
browser = webdriver.Chrome(service= service_object)
browser.get("https://www.google.com/")
print(browser.title)
url1 = browser.title
print(browser.current_url)
url = browser.current_url
if url == url1:
    print("url is correct")
else:
    print("bad")

