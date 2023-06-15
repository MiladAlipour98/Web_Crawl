from selenium import webdriver
from selenium.webdriver.common.by import By
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)

driver.get("https://www.metalsdaily.com/live-prices/gold/")

print(driver.title)

list_to_elastic=[]
vars = ['BID','ASK', '+/-', '%','Circle_UpDown', 'HIGH', 'LOW', 'TIME']

length = len(vars)

for i in range(2,length+1):
    trcount = i
    tdcount = 1
    search_bar = driver.find_element(By.XPATH,
                                     "/html/body/form/div[3]/div[2]/div[1]/div[1]/div/table/tbody/tr[{trCount}]/td[{tdCount}]".format(
                                         trCount=trcount, tdCount=tdcount))
    print('name :', search_bar.text)
    str_detail = search_bar.text+";"
    counter = 0
    for j in range (2,length+2):
        tdcount = j


        search_bar=driver.find_element(By.XPATH, "/html/body/form/div[3]/div[2]/div[1]/div[1]/div/table/tbody/tr[{trCount}]/td[{tdCount}]".format(trCount=trcount,tdCount=tdcount))
        print(vars[counter], search_bar.text)
        str_detail = str_detail + search_bar.text+";"
        counter = counter + 1
    print("Detail:  ",str_detail )
    list_to_elastic.append(str_detail)

lst_detail = []
lst_Name = []
lst_BID = []
lst_ASK = []
lst_PN = []
lst_Percent = []
lst_HIGH = []
lst_LOW = []
lst_TIME = []

for x in range(len(list_to_elastic)):
    d = list_to_elastic[x]
    name = d[:-1]
    lst_detail = name.split(";")
    lst_Name.append(lst_detail[0])
    lst_BID.append(lst_detail[1])
    lst_ASK.append(lst_detail[2])
    lst_PN.append(lst_detail[3])
    lst_Percent.append(lst_detail[4])
    lst_HIGH.append(lst_detail[6])
    lst_LOW.append(lst_detail[7])
    lst_TIME.append(lst_detail[8])

print(lst_Name)
print(lst_BID)
print(lst_ASK)
print(lst_PN)
print(lst_Percent)
print(lst_HIGH)
print(lst_LOW)
print(lst_TIME)

num = 0
for i in range(0, 7):
    num += 1
    doc = {
        'Name': lst_Name[i],
        'BID': lst_BID[i],
        'ASK': lst_ASK[i],
         'PN': lst_PN[i],
    'Percent': lst_Percent[i],
       'HIGH': lst_HIGH[i],
        'LOW': lst_LOW[i],
        'TIME':lst_TIME[i]



    }

    # Save document on elasticsearch
    resp = es.index(index="q1-a", id=num, document=doc)
    print(resp['result'])

    rec = es.get(index='q1-a', id=num)
    print(rec['_source'])

