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


browser.get("https://rahulshettyacademy.com/loginpagePractise/")
#browser.find_element(By.CSS_SELECTOR, ".blinkingText").click()
#//a[contains(text(),'Free Access to InterviewQues/ResumeAssistance/Mate')]
browser.find_element(By.XPATH, "//a[contains(text(),'Free Access to InterviewQues/ResumeAssistance/Mate')]").click()
windowsOpened = browser.window_handles
browser.switch_to.window(windowsOpened[1])
message = browser.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
browser.close()
browser.switch_to.window(windowsOpened[0])
browser.find_element(By.ID, "username").send_keys(var)
browser.find_element(By.ID, "password").send_keys(var)
browser.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(browser, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(browser.find_element(By.CSS_SELECTOR, ".alert-danger").text)
