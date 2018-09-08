# view 為商業邏輯撰寫的一個部分

from django.shortcuts import render
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
https://getbootstrap.com/
並完成首頁和註冊內容的部分
'''
def get_index(request):
    title = 'opencook'
    return render(request, 'index.html', {'title': title})

def get_signup(request):
    return render(request, 'signup.html')



