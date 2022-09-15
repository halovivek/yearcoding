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

browser.get("https://rahulshettyacademy.com/angularpractice/")
browser.maximize_window()
# browser.find_element(By.LINK_TEXT,"Forgot password?").click()
"""
Creating the xpath - by using the form from top to bottom
example. if you check the form- it will drill down from top to bottom
//form/div[1]/input - Here the form is the  top one. in this div[1] is the 
second drill down of the form, in that input is the tag or name of the 
required one. 

For css selector the same one above is followed, but only difference is 
give space instead of // - example (form div:nth-child(1) input)

"""
browser.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']").send_keys("OVM")
browser.find_element(By.XPATH, "//input[@name='email']").send_keys("testing@testing.com")
browser.find_element(By.XPATH, "(//input[@id='exampleInputPassword1'])[1]").send_keys("1234567890")
browser.find_element(By.XPATH, "//input[@id='inlineRadio3']").click()

"""
Select the drop down from the list. 
1. find the element of the list
2. Use Select function in the selenium 
3. store the list of items in a variable
4. select the required from the variable 
5. continue with the execution.
"""
dropdown = Select(browser.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#browser.implicitly_wait(time_to_wait =10)
dropdown.select_by_index(0)
#browser.implicitly_wait(time_to_wait = 10)
dropdown.select_by_visible_text("Female")
"""
Closing the browser and opening a new one
"""
browser.get("https://rahulshettyacademy.com/dropdownspractise/")
