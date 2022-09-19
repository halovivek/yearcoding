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

browser.get("https://rahulshettyacademy.com/AutomationPractice/")
#time.sleep(5)
browser.maximize_window()
time.sleep(5)
"""
Project to check the multiple options check box and store it in the variable
Then select the required option.
"""
checkboxes_list = browser.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes_list))

for checkbox in checkboxes_list:
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()
        break
"""
to find the element using the class name it just enough to type with
'classname'

"""
radiobuttons = browser.find_elements(By.CLASS_NAME, "radioButton")
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
        break
time.sleep(3)

"""
Selecting the radio button using the index since the position of the radio 
buttons will not be changed. 
"""
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
"""
check whether the box is visible or not
"""
assert browser.find_element(By.XPATH,"//input[@id='hide-textbox']").is_displayed()
browser.find_element(By.XPATH ,"//input[@id='hide-textbox']").click()
assert browser.find_element(By.XPATH,"//input[@id='hide-textbox']").is_displayed()
