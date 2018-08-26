#  下載 PTT 八卦版文章標題和作者

# https://www.ptt.cc/ask/over18
# /bbs/Gossiping/index.html
# https://www.ptt.cc/bbs/Gossiping/index.html

import requests
from bs4 import BeautifulSoup

payload ={
	'from': '/bbs/Gossiping/index.html',
	'yes': 'yes'
}  # 模擬一個行為

headers={
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

rs = requests.Session()   # 會話對象讓你能夠跨請求保持某些參數
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)
'''
print(res.text)
# '{"cookies": {"sessioncookie": "123456789"}}'
'''

soup = BeautifulSoup(res.text, 'html.parser')

items = soup.select('.r-ent')  # 去擷取剖析出來的內容; 選擇器用 .r-ent ; ID 用 #
# print(items)

for item in items  # 進一步作擷取的動作
	# print('日期 {}'.format(item.select('.dtaa')[0].text))     # {} 會對到 format 裡面的內容
	print(item.select('.data')[0].text, item.select('.author')[0].text, item.select('title')[0].text)

'''
	Homework: 建立可以爬取多篇表特版文章的網路圖片下載器
		進階: 計算八卦版文章作者發文的數量和標題長度
'''