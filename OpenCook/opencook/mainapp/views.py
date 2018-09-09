# view 為商業邏輯撰寫的一個部分

from django.shortcuts import render
from recipe.models import Recipe

#from django.http import HttpResponse

# Create your views here.

'''
def get_index(request, a, b):
    result = int(a) + int(b)
    return HttpResponse('a + b =' + str(result))
    # function 去做處理, 他把 request 傳進來, 我們回傳一個 response
    # 這邊是引入這個 HttpResponse 這個類別去實例化 HttpResponse 的一個物件回去
    # 這邊是利用引入模組的方法去做這些事情
'''

'''
單元 24
整合 template, 每次都要在這邊去組裝我們的這些東西, 事實上不太直覺, 有些時候我們要把一些工作交由前端工程師去幫我們撰寫
JavaScript, CSS, HTML 這些內容, 這樣的話, 事實上我們要把這些 template 把它切分開來, 更為理想
現在要引入的觀念為 template
'''
# def get_index(request):             # 打造首頁模板, 到 opencook/settings 設計 template 位子, 需更改 settings 的部分
#     return render(request, 'index.html', {'title': 'open cook rock'})       # 使用 render 去整合 templates.  {} 傳參數
#     # 這樣可以動態的去產生我們的內容
#     # 動態網站蠻重要的一個觀念就是說, 由 server side 程式去產生你的內容, 把它塞到 templates 模板裡面去

'''
單元 25 
打造首頁模板借重 bootstrap, 是一個 CSS 的 framework, 提供了許多寫好 CSS 的 component, 可快速套用 CSS 的 class
到 index.html 打造首頁, 完成首頁和註冊內容 (signup.html) 的部分
https://getbootstrap.com/
https://getbootstrap.com/docs/3.3/getting-started/
'''

def get_index(request):
    title = 'opencook'
    recipes = Recipe.objects.all()  # 把 recipe 資料引入
    for recipe in recipes:
        print(recipe.title)
    return render(request, 'index.html', {'title': title})

def get_signup(request):
    return render(request, 'signup.html')

'''
單元 26 資料庫的一些 schema 建置
資料庫為一種長期儲存資料的方法, 和一般在寫程式宣告變數去暫時性儲存資料是不一樣的
資料庫分為 RBD(關聯式資料庫), NoSQL .....
本單元要講的是 SQLite, 關聯式資料庫最重要的一個特色是 table 和 table 之間的一些關聯
使用 Django Model 優點: 
1. 透過資料庫轉換相當方便, 透過 setting.py 去 setting 資料庫到我們要對應哪一種的資料庫,
可方便的去移轉我們的料庫
2. ENGINE 使用的資料庫引擎, 可以設定 MySQL, SQLite 或是 pgSQL
------------------------------------------------------
Python Django ORM 入門
** 物件關聯對映 (ORM = Object Relation Mapping) 是一種程式設計技術, 用於實現物件導向編程語言裡不同類型系統的資料之間的轉換
** ORM 可以讓你使用物件方式而非 SQL 的方式操作資料庫, 但複雜的情況還是得需要用到 SQL 語法
**操作資料庫一般基本操作 CRUD, create, read, update, delete 的操作
SQL vs ORM
-create
． INSERT INTO Recipe ("title") VALUES ("玉米濃湯") ----- SQL
． Recipe.objects.create(title='玉米濃湯')          ----- ORM
QuerySet API (ORM 方式操作)
1. create: Recipe.objects.create(title='玉米濃湯')
2. read: Recipe.objects.all()/Recipe.objects.get()/Recipe.objects.filter()
3. update: Recipe.objects.filter(title='玉米濃湯').update(title='soup')/Recipe.update(title='soup')
4. delete: Recipe.objects.filter().delete()/Recipe.delete()
'''

'''
Homework 單元26:
        建立 OpenCook 的 recipe model 
'''


