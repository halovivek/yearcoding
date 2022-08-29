from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
time.sleep(5)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'box') and text()='Rome']")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[starts-with(@id, 'box') and text()='South Korea']")))
ActionChains(driver).drag_and_drop(drag, drop).perform()


'''drg = driver.find_element(By.XPATH, "//*[@id='dropContent']//div[@class='dragableBox' and @id='box5']")
drp = driver.find_element(By.XPATH, "//*[@id='countries']//div[@class='dragableBoxRight' and @id='box105']")
ActionChains(driver).drag_and_drop(drg, drp).perform()
time.sleep(5)'''
#driver.quit()