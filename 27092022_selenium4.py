from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
#from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
options = Options()
options.binary_location = r'/usr/bin/firefox'
driver = webdriver.Firefox(executable_path=r'/home/halovivek/Downloads/Education', Options=options)
driver.get('http://google.com/')