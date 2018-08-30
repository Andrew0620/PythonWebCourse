import requests
import json
import matplotlib.pyplot as plt

url = 'http://data.fda.gov.tw/cacheData/35_3.json'

res= requests.get(url)

#print(res.text)
items =json.loads(res.text)  # 把 json 檔引入進來, 變成 python 可以操作的一個方法

