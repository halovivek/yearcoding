from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(service=s)
#browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.google.com")
print(browser.title)
print(browser.current_url)
