#https://www.nseindia.com/market-data/live-equity-market
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

browser.get("https://www.nseindia.com/")
print(browser.title)
#
#//a[normalize-space()='Equity & SME Market']
action.move_to_element(browser.find_element(By.XPATH, "(//a[normalize-space()='Market Data'])[1]")).perform()
action.move_to_element(browser.find_element(By.XPATH, "//a[normalize-space()='Equity & SME Market']")).click().perform()
print(browser.title)
