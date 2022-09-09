from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
#from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
s= Service(ChromeDriverManager().install())
#s= Service(GeckoDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
#browser = webdriver.Firefox(service=s)
browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://rahulshettyacademy.com/")
print(browser.title)
print(browser.current_url)
browser.get("https://rahulshettyacademy.com/learning-path")
browser.back()
browser.forward()
browser.minimize_window()
browser.maximize_window()
browser.get("https://www.google.com")
print(browser.current_url)
#browser.close()


