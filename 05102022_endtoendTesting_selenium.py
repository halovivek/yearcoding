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
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.maximize_window()
browser.implicitly_wait(5)
"""
End to end testing. 
Select the particular item, click to select and then contiune further.
"""
# opening the browser and website
browser.get("https://rahulshettyacademy.com/angularpractice/")
browser.find_element(By.XPATH, "//a[normalize-space()='Shop']").click()
# //div[@class='card h-100'] it will give you the list of cards.
mobile_items = browser.find_elements(By.XPATH, "//div[@class='card h-100']")
for mobile in mobile_items:
    productname = mobile.find_element(By.XPATH,"//div[@class='card h-100']/div/h4/a").text
    if productname == "Blackberry":
        mobile.find_element(By.XPATH, "(//button[contains(text(),'Add')])[4]").click()


browser.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
print(browser.title)

#//div[@class='card h-100']/div/h4/a This is drill down of the mobile name.
