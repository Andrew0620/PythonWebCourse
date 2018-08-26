# 功能設計: 爬取露天拍賣商品價格和名稱資訊

import requests
from bs4 import BeautifulSoup

url= 'https://find.ruten.com.tw/c/00110002?style=list'

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

res.get(url, headers=headers)

print(res.text)