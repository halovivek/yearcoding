from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

'''from webdriver_manager.chrome import ChromeDriverManager
driver.implicitly_wait(0.5)
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
#driver = webdriver.Chrome(ChromeDriverManager().install())'''

driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path="/home/halovivek/Documents/Automation/selenium_driver/chromedriver.exe")
#driver = webdriver.Chrome()"
driver.maximize_window()
driver.get("https://www.google.com")
