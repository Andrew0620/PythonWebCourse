# 功能設計: 爬取露天拍賣商品價格和名稱資訊

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://find.ruten.com.tw/c/00110002?bidway=all&style=list'

headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

res = requests.get(url, headers=headers)
#print(res.text)
'''
soup = BeautifulSoup(res.text, 'html.parser')

result = soup.select('.search_form s_list')

print(result)

# 無法搜尋到網站資訊, 可能網站用了一些 JavaScript 的渲染, 或是它本身去阻擋一些ㄧ般的爬蟲機制, 
# 那我們可以嘗試用更像真人的一種方式去爬取我們的網頁, 那我們這時候會使用 selenium 這一個模擬瀏覽器行為的自動化工具
# 那搭配 PhantomJS, PhantomJS 事實上是一個瀏覽器 WebKit 渲染的一個引擎, 那它事實上可以去執行我們的 JavaScript,
# 也可以去操作我們的 DOM, 非常方便的工具, 更重要的是它是 headless, 沒有介面的一個工具,
# 可能一班的人使用它會去搭配像 Firefox 或 chrome 的一個 driver, 事實上我們也可以搭配這樣的 driver,
# 這樣的行為在執行上是沒有效率的, 因為它會跳出一個瀏覽器去執行你下達的指令
'''

# 這邊我們使用 selenium 和 PhantomJS
browser = webdriver.PhantomJS(executable_path='./phantomjs.exe')  # phantomjs 若沒放在同一資料夾, 需指定路徑去執行
browser.get(url)

print(browser.page_source)

