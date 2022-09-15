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

browser.get("https://www.makemytrip.com/")
#time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.find_element(By.ID, "fromCity").click()

#browser.find_element(By.XPATH, "//input[@placeholder='From']").click()
"""
1. Click the autosuggestion box 
2. put the autosuggetion box to display the record 
3. we need time to display all the records, so we are putting time.sleep
4. then select the required text and close it.
"""
time.sleep(5)
#browser.find_element(By.XPATH, "//input[@placeholder='From']").send_keys("ind")
#browser.find_element(By.ID, "fromCity").clear()
browser.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("Ind")
#browser.find_element(By.CSS_SELECTOR, ".hsw_sectionTitle.font12.latoBlack.greyText").send_keys("ind")
places = browser.find_elements(By.CSS_SELECTOR, "#react-autowhatever-1")
#print(browser.find_elements(By.CSS_SELECTOR, "#react-autowhatever-1").__getattribute__("value"))
print(len(places))
# print(places)
for place in places:
    if place.text == "Mangalore":
        place.click()
        break
# Need to select and close the pop up