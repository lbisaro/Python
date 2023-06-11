from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
options = Options()
options.add_argument('--headless')

service = Service(executable_path=CHROMEDRIVER_PATH)

driver = webdriver.Chrome(service=service,options=options)
driver.get("https://www.google.com")
print(driver.title)
driver.close()


