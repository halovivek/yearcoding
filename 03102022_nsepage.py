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
symbol_lists =[]
"""
Opening the browser and navigate to the website

"""

browser.get("https://www.nseindia.com/market-data/live-equity-market")
print(browser.title)

symbol_lists = browser.find_elements(By.XPATH,"//tbody").text
for symbol_list in symbol_lists:
    print(symbol_lists)
