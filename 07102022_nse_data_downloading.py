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
import pandas as pd
from bs4 import BeautifulSoup

"""
Browser preparation 
"""
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.maximize_window()
browser.implicitly_wait(5)
stocks_list = []
"""
Opening the Nse website.
Navigate to link and click it.
get all stocks list.
"""
browser.get("https://www.nseindia.com/market-data/live-equity-market")
print(browser.title)
#browser.get("https://www.nseindia.com")
time.sleep(5)
action = ActionChains(browser)
# live_market_section = browser.find_element(By.XPATH, '//*[@id="main_livemkt"]/a')
# action.move_to_element(live_market_section).perform()
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')
#soup = BeautifulSoup(html,'lxml')
time.sleep(7)
result = soup.find('table',{'class': 'tablesorter'})
table_rows = result.find_all('tr')

l = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text for tr in td]
    l.append(row)

# Creating the table using pandas
equity_derivatives_table = pd.DataFrame(l, columns=["Symbol", "Open", "High", "Low"])
equity_derivatives_table = equity_derivatives_table.drop([0], axis=0)
table_rows = result.find_all('tr')
equity_derivatives_table.to_csv("NSE.csv", index=0)

