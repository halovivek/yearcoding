import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=s, options=chrome_options)
"""
Above the basic setup to run the chrome browser
Below the project starts.
Find the locators and resetting the password
"""
name = "OVM"
browser.get("https://rahulshettyacademy.com/AutomationPractice/")
#time.sleep(5)
browser.maximize_window()
time.sleep(5)


"""
Handling the Java script and java pop ups in the page.
Popus cannot be handled by just ordinary method. Need to use the alert method
to handle the alerts.
create a variable to handle the alert methods. the variable will act as the object like 
browser. to handle the things.

"""
browser.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
browser.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()

browser.find_element(By.XPATH, "//input[@id='name']").send_keys(name)
browser.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
alert.dismiss()



