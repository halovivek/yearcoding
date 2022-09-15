from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

browser.get("https://rahulshettyacademy.com/client")
browser.maximize_window()
browser.find_element(By.LINK_TEXT,"Forgot password?").click()
"""
Creating the xpath - by using the form from top to bottom
example. if you check the form- it will drill down from top to bottom
//form/div[1]/input - Here the form is the  top one. in this div[1] is the 
second drill down of the form, in that input is the tag or name of the 
required one. 

For css selector the same one above is followed, but only difference is 
give space instead of // - example (form div:nth-child(1) input)

"""
browser.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
browser.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys(123456)
browser.find_element(By.CSS_SELECTOR, "form div:nth-child(3) input").send_keys(123456)
browser.find_element(By.XPATH,"//button[contains(text(),'Save New Password')]").click()


