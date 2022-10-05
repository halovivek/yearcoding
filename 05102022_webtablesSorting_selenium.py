import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.maximize_window()
browser.implicitly_wait(5)

# opening the browser and website
browser.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
"""
Go to the page.
Click the list of items to ten
Get the input from the tables
Then sort according to the ascending order.
Need to store the value in a variable and compare to check the values.
//span[@class='sort-icon sort-ascending']
//span[@class='sort-icon sort-']
//span[normalize-space()='Veg/fruit name']
"""
browser.find_element(By.ID, "page-menu").click()
browser.find_element(By.XPATH, "//option[@value='10']").click()
browser.find_element(By.XPATH, "//span[normalize-space()='Veg/fruit name']").click()
time.sleep(3)
browser.find_element(By.XPATH, "//span[@class='sort-icon sort-ascending']").click()
time.sleep(3)
browser.find_element(By.XPATH, "//span[@class='sort-icon sort-descending']").click()
"""
//tr/td[1] - First one is the whole body //tr and in that td[1] is the required coloumn
we need to store in the list
sort using python method. sort command then compare with the browser values
create a variable with empty list to store the data and get the text from the list and append it in the variable
then create a another variable with sort. 
"""
vegitalbesbrowser = browser.find_elements(By.XPATH, "//tr/td[1]")
print(len(vegitalbesbrowser))
originalData = []
for veg in vegitalbesbrowser:
    originalData.append(veg.text)

checkthelist = originalData.copy()
print(originalData)
originalData.sort()
assert checkthelist == originalData



