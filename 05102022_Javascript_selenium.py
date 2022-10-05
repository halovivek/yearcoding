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
browser.get("https://the-internet.herokuapp.com/")
# Click Inspect - console - type the required to scroll down. you can give (x,y) -
# x - breath value, and y is height value - you need to just tell the selenium
# that you are executing the Javascript.

browser.execute_script("scrollBy(0,document.body.scrollHeight);")
browser.get_screenshot_as_file("test.png")
#test