import requests
from bs4 import BeautifulSoup

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}   # 讓網路爬蟲像真人的一個模式, 因為有些網頁管理員會擋    # Mozilla 是瀏覽器的一個內核

res = requests.get('https://www.ptt.cc/bbs/Beauty/M.1535220756.A.4C0.html', headers=headers)  # get & post 差異

'''
print(res.text)  # 剖析網頁內容
'''
soup = BeautifulSoup(res.text, 'html.parser')  # html.parser 使用的剖析器

images = soup.select('a[href^=https://imgur]')   # ^= 意思是 "開頭="

print(images)