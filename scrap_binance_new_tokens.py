from datetime import datetime


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
options = Options()
options.add_argument('--headless')

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(15)

url = 'https://www.binance.com/es/support/announcement/nuevas-criptos-listadas?c=48&navId=48'
driver.get(url)
print(driver.title)
print('-------->')

now = datetime.now()
str_datetime = now.strftime("%Y-%m-%d %H:%M")

tags = driver.find_elements(By.XPATH,'//*[@id="__APP"]/div/div/main/div[2]/div[2]/div[2]/section/div[2]/div[1]/div/a')
for tag in tags[:3]:
    link = tag.get_attribute('href')
    
    text = tag.text
    notice = text[0:-10]
    date = text[-10:]
    print(date,"\n"+notice,"\n"+link)
    print('-->')
print('<------')


driver.close()