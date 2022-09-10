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
browser = webdriver.Chrome(service=s)
browser.maximize_window()
browser.get("https://www.investing.com/")
print(browser.title)
#browser.find_element(By.xpath="//header/div[1]/div[1]/div[3]/div[1]/input[1]")

#browser.find_element(By.XPATH="//header/div[1]/div[1]/div[3]/div[1]/input[1]").click()
