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
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s, options=chrome_options)
"""
Above the basic setup to run the chrome browser
Below the project starts.

"""
"""
Need to close the pop-up browser and then we need to proceed with the execution
1. check the auto pop-up and close it
2. check anymore pop- up and close it
3. then run the execution.
"""
browser.get("https://www.makemytrip.com/")
#time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.find_element(By.ID, "fromCity").click()
browser.find_element(By.ID,"fromCity").clear()
browser.find_element(By.ID, "fromCity").send_keys("ind")
autosuggest_places = browser.find_elements(By.XPATH,"//div[@class='react-autosuggest__section-container react-autosuggest__section-container--first']")
print(len(autosuggest_places))

browser.find_elements(*(By.XPATH,"//div[@class='react-autosuggest__section-container react-autosuggest__section-container--first']"))