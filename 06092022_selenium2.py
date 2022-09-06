import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
s=Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=s)

browser.implicitly_wait(5)
browser.get("https://kite.zerodha.com/")
browser.maximize_window()
browser.find_element(By.XPATH, "//*[@id='userid']").send_keys("DV1815")
browser.find_element(By.XPATH,"//*[@id='password']").send_keys("Guru@1234")
browser.find_element(By.XPATH,"//button[@type='submit']").click()
print(browser.title)
browser.find_element(By.XPATH,"//*[@id='pin']").send_keys("235059")
browser.find_element(By.XPATH,"//button[@type='submit']").click()
#Browser will print the title of the window
print(browser.title)
browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[4]/button[1]/span[1]").click()
#browser.switch_to.frame("chart-iframe")
#browser.find_element(By.ID, "//*[@id='popout_chart']").click()
#Browser will print the title of the window
print(browser.title)
#browser.quit()