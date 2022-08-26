from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time
#browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser.maximize_window()
browser.get("https://opensource-demo.orangehrmlive.com")
browser.implicitly_wait(5)
print(browser.title)
browser.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
browser.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
browser.find_element_by_xpath("//*[@id='btnLogin']").click()
#browser.find_element_by_xpath()

#//*[@id="btnLogin"]


#browser.quit()