import config
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import mysql.connector
from mysql.connector import Error

db = mysql.connector.connect(host=config.DB_HOST,
                                        database=config.DB_NAME,
                                        user=config.DB_USER,
                                        password=config.DB_PASS)


CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
options = Options()
options.add_argument('--headless')

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(15)
alerts = []

url = 'https://www.binance.com/es/support/announcement/nuevas-criptos-listadas?c=48&navId=48'
driver.get(url)
print(driver.title)
print('-------->')

now = datetime.now()
str_datetime = now.strftime("%Y-%m-%d %H:%M")

tags = driver.find_elements(By.XPATH,'//*[@id="__APP"]/div/div/main/div[2]/div[2]/div[2]/section/div[2]/div[1]/div/a')
for tag in tags:
    link = tag.get_attribute('href')
    
    text = tag.text
    notice = text[0:-10]
    date = text[-10:]
    alerts.append((date,notice,link,1))
    print(date,"\n"+notice,"\n"+link)
    print('-->')
print('<------')



cursor = db.cursor()

sql = "INSERT INTO binance_alerts (date, text, link, type) VALUES (%s, %s, %s, %s)"

try:  
  cursor.executemany(sql, alerts)
  print(cursor.rowcount, "records inserted.")
except:
  print('Something went wrong.')

db.commit()



cursor.close()
db.close()

driver.close()
