from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
browser.implicitly_wait(5)
print(browser.title)


source_element = browser.find_element(By.XPATH, "//*[@id='DHTMLgoodies_dragableElement5']")
target_element = browser.find_element(By.XPATH,"//*[@id='box106']")
actions = ActionChains(browser)
actions.drag_and_drop(source_element,target_element).perform()






#browser.quit()