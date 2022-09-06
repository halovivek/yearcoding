from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#from webdriver_manager.chrome import ChromeDriverManager
def test_me(my_name):
    s=Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(r'C:\Drivers\chromedriver.exe')
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("https://kite.zerodha.com/")


#from selenium.webdriver.chrome.service import Service
import os
#import self as self
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#path = (r'C:\Drivers\chromedriver.exe')
#s = Service(path)
#driver = webdriver.Chrome(service=s)
# browser.maximize_window()
# browser.find_element(By.XPATH, "//*[@id='userid']").send_keys("DV1815")
# browser.find_element(By.XPATH,"//*[@id='password']").send_keys("Guru@1234")
# browser.find_element(By.XPATH,"//button[@type='submit']").click()
# print(browser.title)
# browser.find_element(By.XPATH,"//*[@id='pin']").send_keys("235059")
# browser.find_element(By.XPATH,"//button[@type='submit']").click()
# print(browser.title)
#
# browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
# browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[4]/button[1]/span[1]").click()
# #browser.switch_to.frame("chart-iframe")
# browser.find_element(By.ID, "//*[@id='popout_chart']").click()
# print(browser.title)
# #browser.quit()