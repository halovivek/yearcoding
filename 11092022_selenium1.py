# https://rahulshettyacademy.com
# Get title name
# https://rahulshettyacademy.com/angularpractice/
# Get title name
# xpath - //body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]
# email
# //body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]
# password
# //body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]
# check box
# //input[@id='exampleCheck1']
# select box
# //select[@id='exampleFormControlSelect1']
# employement status
# //input[@id='inlineRadio2']
# calender
# //body/app-root[1]/form-comp[1]/div[1]/form[1]/div[7]/input[1]

"""
Importing all the services which required to run
1. Importing the selenium webdriver
2. Importing the common keys
3. importing the chrome browser driver to run the chrome drivere
4. Importing the common keys to run the common attributes which is useful to run
the system
5. Downloading and installing the driver through the Download manager, it will
help automatically to download the drivers and it will run the chrome browser
6. detach is used to stay the browser alive for the  system
7. After all procedueres the broswer is started to work with.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

"""
The browser will be started.
"""
browser = webdriver.Chrome(service=s, options=chrome_options)
browser.maximize_window()
# chrome_options = Options()
# chrome_options.add_experimental_option("detach",True)
browser.get("https://rahulshettyacademy.com")
print(browser.title)
browser.get("https://rahulshettyacademy.com/angularpractice/")
print(browser.title)
browser.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[1]/input[1]").send_keys("OVM")
browser.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[2]/input[1]").send_keys("ovm@gmail.com")
browser.find_element(By.ID,"exampleInputPassword1").send_keys("123456789")
browser.find_element(By.XPATH,"//input[@id='exampleCheck1']").click()
browser.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']").click()
browser.find_element(By.XPATH,"//input[@id='inlineRadio2']").click()
browser.find_element(By.XPATH,"//body/app-root[1]/form-comp[1]/div[1]/form[1]/div[7]/input[1]").send_keys("01/01/2000")
browser.implicitly_wait(20000)