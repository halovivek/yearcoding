import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.implicitly_wait(5)
"""
Above the basic setup to run the chrome browser
Below the project starts.
Find the locators and resetting the password
we are using the implicit wait instead of sleep
Implicit wait will wait until the program loads. it saves time.
"""
#name = "OVM"
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#time.sleep(5)
browser.maximize_window()
#time.sleep(3)
# browser.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("a")
# time.sleep(3)
# items_list = browser.find_elements(By.XPATH, "//div[@class='products']/div")
# print(len(items_list))
# count = len(items_list)
# assert count > 0
# browser.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").clear()
# browser.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("a")
# time.sleep(3)
# items_list = browser.find_elements(By.XPATH, "//div[@class='products']/div")
# print(len(items_list))
# count = len(items_list)
# assert count > 0
browser.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").clear()
browser.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ca")
time.sleep(3)
items_list = browser.find_elements(By.XPATH, "//div[@class='products']/div")
print(len(items_list))
count = len(items_list)
assert count > 0
"""
Chain link - 
Once you get all the list of items, we need to find the add to cart button and click it
For that we dont need the browser.find_element , we need to find the element
from the result variable.
WE ARE GOING TO USE explit wait ,until the required element is loaded.
in explict wait, you need to declare a variable , then pass the argument which needs to be
done. then you need to import a package to support that. 
"""
for item_list in items_list:
    item_list.find_element(By.XPATH, "div/button").click()

"""
The above will check all the items and it will click the buttons in all carts
"""

browser.find_element(By.XPATH, "//img[@alt='Cart']").click()
browser.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
#time.sleep(3)
browser.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
browser.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promotext = browser.find_element(By.CLASS_NAME, "promoInfo").text
print(promotext)
assert promotext == "Code applied ..!"

