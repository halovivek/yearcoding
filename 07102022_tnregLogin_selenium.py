import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()
browser.implicitly_wait(5)
"""
End to end testing. 
Select the particular item, click to select and then contiune further.
"""
# opening the browser and website
browser.get("https://tnreginet.gov.in/portal/")
browser.find_element(By.XPATH, "(//a[@id='fontSelection'])[1]").click()
#//input[@id='username']
#//input[@id='password']
browser.find_element(By.XPATH, "//input[@id='username']").send_keys("halovivek")
browser.find_element(By.XPATH, "//input[@id='password']").send_keys("Guru@235059")
time.sleep(10)
browser.find_element(By.XPATH, "//input[@value='Sign In']").click()
print(browser.title)
