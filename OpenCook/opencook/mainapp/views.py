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
整合 template, 每次都要在這邊去組裝我們的這些東西, 事實上不太直覺, 有些時候我們要把一些工作交由前端工程師去幫我們撰寫
JavaScript, CSS, HTML 這些內容, 這樣的話, 事實上我們要把這些 template 把它切分開來, 更為理想
現在要引入的觀念為 template
'''
def get_index(request):             # 打造首頁, 到 opencook/settings 設計 template 位子, 需更改 settings 的部分
    return render(request, 'index.html', {'title': 'open cook rock'})       # 使用 render 去整合 templates.  {} 傳參數



