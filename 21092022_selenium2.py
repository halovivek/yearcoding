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
Compare the expected results with actual results
for ca selection it should display only Cauliflower - 1 Kg
Carrot - 1 Kg
Capsicum
Cashews - 1 Kg
Need to store in a list.
Get the list from the display and store it in a new list.
compare the both list and confirm pass or fail.
"""
expectedlist = ['Cauliflower - 1 Kg', 'Carrot - 1 Kg', 'Capsicum', 'Cashews - 1 Kg']
actuallist =[]
print(expectedlist)
"""
The above two list, one is expected list and other one is actual list.

"""
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#time.sleep(5)
browser.maximize_window()
browser.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").clear()
browser.find_element(By.XPATH,"//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ca")
time.sleep(3)
items_list = browser.find_elements(By.XPATH, "//div[@class='products']/div")

print(len(items_list))
count = len(items_list)
assert count > 0

#the append in the actuallist will add the items which is found
for item_list in items_list:
    actuallist.append(item_list.find_element(By.XPATH, "h4").text)
    item_list.find_element(By.XPATH, "div/button").click()

assert expectedlist == actuallist

print(actuallist)

browser.find_element(By.XPATH, "//img[@alt='Cart']").click()
browser.find_element(By.XPATH,"//button[normalize-space()='PROCEED TO CHECKOUT']").click()
#sum Validation
prices = browser.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
time.sleep(3)
sums = 0
for price in prices:
    sums = sums + int(price.text)

print(sums)

total_amount = int(browser.find_element(By.CSS_SELECTOR, ".totAmt").text)


if sums == total_amount:
    print("Both values are correct", sums)
else:
    print("calculation is wrong")


time.sleep(3)
browser.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
browser.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
promotext = browser.find_element(By.CLASS_NAME, "promoInfo").text
print(promotext)
assert promotext == "Code applied ..!"
#instead of getting the integer value , convert it to float for decimal value
discounted_value = float(browser.find_element(By.XPATH, "//span[@class='discountAmt']").text)
assert discounted_value < total_amount

#testing


browser.close()

