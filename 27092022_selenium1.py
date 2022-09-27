import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.binary_location = r"/usr/bin/"
options = webdriver.FirefoxOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

#browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(5)


"""
Here we are going to switch between windows.


"""
browser.get("https://the-internet.herokuapp.com/windows")
print(browser.title)
browser.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
windows = browser.window_handles
browser.switch_to.window(windows[1])
print(browser.find_element(By.XPATH, "//h3[normalize-space()='New Window']").text)
browser.close()
#this will close the child window and it will move to the new window
browser.switch_to.window(windows[0])
print(browser.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text)
test = browser.find_element(By.CSS_SELECTOR,"div[class='example'] h3").text
assert test == "Opening a new window"

