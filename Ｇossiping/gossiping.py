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

print(items)
