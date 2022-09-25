import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(service= FirefoxService(GeckoDriverManager().install()))
# driver = webdriver.Firefox(service= FirefoxService(GeckoDriverManager().install()),options=options)
firefox_binary = FirefoxBinary('/usr/bin/firefox/')
driver = webdriver.Firefox(firefox_binary=firefox_binary)
options = webdriver.FirefoxOptions()
#options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

URL ='https://www.rahulshettyacademy.com/AutomationPractice'
driver.get(URL)
time.sleep(3)
