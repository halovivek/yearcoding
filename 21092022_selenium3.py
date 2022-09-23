import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
action = ActionChains(browser)
# //button[@id='mousehover']
# Open the webpage
browser.get("https://rahulshettyacademy.com/AutomationPractice/")
browser.maximize_window()
"""
Here we are going to use the mouse operations by Action buttons
we need to import the action buttons
we need to declare the driver inside the path
Use the variable to get the details
you need to use perform at end of the action to work
"""
action.move_to_element(browser.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.context_click(browser.find_element(By.XPATH, "//a[normalize-space()='Top']")).perform()
