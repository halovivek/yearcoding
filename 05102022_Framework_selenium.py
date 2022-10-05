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
browser.get("https://the-internet.herokuapp.com/iframe")
# switch to the frame to enter
browser.switch_to.frame("mce_0_ifr")
browser.find_element(By.ID, "tinymce").clear()
browser.find_element(By.ID, "tinymce").send_keys("I am automating the frame input")
browser.switch_to.default_content()
#switch back to original content.
print(browser.find_element(By.CSS_SELECTOR, "h3").text)
