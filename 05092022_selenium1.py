from selenium  import webdriver
#from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
service_object = Service("C:\Drivers\chromedriver.exe")
option = webdriver.ChromeOptions("C:\Drivers\chromedriver.exe")
option.add_argument("--incognito")
driver = webdriver.Chrome(options=option)
driver.get("https://www.yahoo.com")
