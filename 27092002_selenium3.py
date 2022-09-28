import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.firefox import GeckoDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options = webdriver.FirefoxOptions()
options.binary_location = r"/usr/bin/"
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
capabilities = webdriver.FirefoxOptions().to_capabilities()
options.set_capability("cloud:options", capabilities)
service = FirefoxService(log_path=os.devnull,)
browser = webdriver.Firefox(service= FirefoxService(GeckoDriverManager().install()), options=options)
#browser = webdriver.Firefox(service=service,options=options,)



browser.maximize_window()
browser.implicitly_wait(5)
browser.get("https://the-internet.herokuapp.com/windows")
print(browser.title)

