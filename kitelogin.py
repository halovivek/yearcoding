from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.implicitly_wait(5)
'''window_before = browser.window_handles[0]
window_after = browser.window_handles[1]'''

browser.get("https://kite.zerodha.com/")
browser.maximize_window()
browser.find_element(By.XPATH, "//*[@id='userid']").send_keys("DV1815")
browser.find_element(By.XPATH,"//*[@id='password']").send_keys("Guru@1234")
browser.find_element(By.XPATH,"//button[@type='submit']").click()
print(browser.title)
browser.find_element(By.XPATH,"//*[@id='pin']").send_keys("235059")
browser.find_element(By.XPATH,"//button[@type='submit']").click()
print(browser.title)

browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/span[1]").click()
browser.find_element(By.XPATH,"//body/div[@id='app']/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]/span[4]/button[1]/span[1]").click()
#browser.switch_to.frame("chart-iframe")
browser.find_element(By.ID, "//*[@id='popout_chart']").click()


#frames = browser.find_elements(By.XPATH, "//iframe[@id='chart-iframe']")
#browser.switch_to_frame(frames)""

#browser.find_element(By.ID, "@id='popout_chart'").click()

#browser.find_element(By.XPATH,"span[@class='icon icon-trending-up']")
#browser.switch_to_frame(browser.find_element(By.XPATH, "//iframe[@id='chart-iframe']"))


print(browser.title)

#//*[@id="popout_chart"]


#browser.switch_to().frame(0)
#browser.find_element(By.XPATH, "//*[@id='popout_chart']").click()
#browser.find_element(By.XPATH,"//div[@class='ciq-nav']").click()
#browser.save_screenshot("/home/halovivek/Documents/Automation/Home.png")
#browser.find_element(By.CSS_SELECTOR("div.vddl-draggable:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1) > span:nth-child(1)")).click()
##browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/div/div[2]/div[2]/div/div/ul/li[9]/a").click()
#webdriver.wait(5)
#browser.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div/div[2]/div/div[1]/div/span/span[4]/button/span").click()
#browser.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div/div[2]/div").click()
#browser.find_element(By.XPATH,"//*[@id='app']/div[2]/div[1]/div/div[2]/div/div[1]/div/span/span[4]/button/span").click()
#browser.find_element()
#browser.close()
#browser.get("https://www.nseindia.com/market-data/live-equity-market")
#time.sleep(5)
#print(browser.title)
#browser.quit()