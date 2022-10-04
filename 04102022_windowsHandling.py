import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.maximize_window()
browser.implicitly_wait(5)
symbol_lists = []
action = ActionChains(browser)
"""
Opening the browser and navigate to the website

"""

browser.get("https://the-internet.herokuapp.com/windows")
print(browser.title)
"""
Clicking the new window link and closing it
"""
browser.find_element(By.CSS_SELECTOR,"a[href='/windows/new']").click()
#//h3[normalize-space()='New Window']
totalWindows = browser.window_handles
browser.switch_to.window(totalWindows[1])
print(totalWindows)
print(len(totalWindows))
print(browser.find_element(By.XPATH,"//h3[normalize-space()='New Window']").text)
print(browser.title)