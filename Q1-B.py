from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from elasticsearch import Elasticsearch

#Connect to the elasticsearch
es = Elasticsearch('http://localhost:9200')

#Browser does not open
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

#links of coins
links=['http://www.tsetmc.com/loader.aspx?ParTree=151311&i=57675016001659793',
       'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=6183017539978894',
       'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=10427474943853556',
       'http://www.tsetmc.com/loader.aspx?ParTree=151311&i=56394387537858740']

num=0
#Connect to the each links and Get data of coins
for g in links:
     driver.get(g)
     
     #10 sec for make sure to connect to the site
     time.sleep(10)
     
     #Get data by Xpath
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[1]")
     print ('نام و ساعت:',search_bar.text)
     name = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[1]")
     print ('خريد:',search_bar.text)
     buy = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[2]")
     print ('معامله:',search_bar.text)
     orde=search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[4]/td[1]")
     print ('اولين:',search_bar.text,'\n')
     first = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[4]/td[2]")
     print ('پاياني:',search_bar.text,'\n')
     end = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[2]/td[3]")
     print ('فروش:',search_bar.text)
     sell = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[1]/table/tbody/tr[4]/td[3]")
     print ('ديروز:',search_bar.text)
     yest = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[3]/table/tbody/tr[1]/td[2]")
     print ('تعداد معاملات:',search_bar.text)
     numb = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[3]/table/tbody/tr[2]/td[2]/div")
     print ('حجم معاملات:',search_bar.text)
     volul = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[3]/table/tbody/tr[3]/td[2]/div")
     print ('ارزش معاملات:',search_bar.text)
     corr = search_bar.text
     search_bar=driver.find_element(By.XPATH, "/html/body/div[4]/form/div[3]/div[2]/div[1]/div[3]/div[3]/table/tbody/tr[4]/td[2]/div")
     print ('ارزش بازار:',search_bar.text)
     bazzar = search_bar.text

     #Creat document of schema
     num+=1
     doc = {
     'نام و ساعت':name,
     'خريد':buy,
     'معامله':orde,
     'اولين':first,
     'پاياني':end,
     'فروش':sell,
     'ديروز':yest,
     'تعداد معاملات':numb,
     'حجم معاملات':volul,
     'ارزش معاملات':corr,
     'ارزش بازار':bazzar
        }
     
     #Save document on elasticsearch
     resp = es.index(index="q1-b", id=num, document=doc)
     print(resp['result'])

     rec = es.get(index='q1-b', id=num)
     print(rec['_source'])

