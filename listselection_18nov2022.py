import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
browser.maximize_window()
browser.implicitly_wait(5)

#get the list of items in the drop down and select
browser.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
dropdown = browser.find_element(By.NAME, "UserTitle")
dd = Select(dropdown)
dd.select_by_index(1)
time.sleep(3)
dd.select_by_index(2)
time.sleep(3)
dd.select_by_index(7)
time.sleep(3)
dd.select_by_index(5)
