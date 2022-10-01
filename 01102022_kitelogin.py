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

#s = Service(ChromeDriverManager().install())
#chrome_options = Options()
# chrome_options.add_experimental_option("detach",True)
#browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
browser.implicitly_wait(5)


"""
Opening the kite browser to first page.
"""
browser.get("https://kite.zerodha.com/")
print(browser.title)
browser.find_element(By.XPATH,"//input[@id='userid']").send_keys("DV1815")
browser.find_element(By.XPATH,"//input[@id='password']").send_keys("Guru@1234")
browser.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
browser.find_element(By.XPATH,"//input[@placeholder='••••••']").send_keys(235059)
browser.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()
print(browser.title)
browser.find_element(By.XPATH,"//span[@class='nice-name'][normalize-space()='NIFTY 50']").click()
browser.find_element(By.XPATH,"//span[@class='icon icon-trending-up']").click()
print(browser.title)


#//span[@class='nice-name'][normalize-space()='NIFTY 50']
#//span[@class='icon icon-trending-up']


"""
browser.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
windows = browser.window_handles
browser.switch_to.window(windows[1])
print(browser.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
browser.close()
#this will close the child window and it will move to the new window
browser.switch_to.window(windows[0])
print(browser.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text)
test = browser.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text
assert test == "Opening a new window"
"""
browser.find_element(By.XPATH,"//span[@class='user-id']").click()
browser.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

