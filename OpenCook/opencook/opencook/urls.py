"""opencook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

'''
單元 24: Django URL 管理與商業邏輯
進一步探討 views 與 urls 之間的一些關係, 如何去處理 request, 又如何回傳 response
最後整合我們的 template 去打造我們 OpenCook 的首頁和註冊頁面
'''

from django.contrib import admin
from django.conf.urls import url

from mainapp.views import get_index, get_signup, post_signup, post_login, post_logout
from recipe.views import get_recipes_api, get_create_recipe, post_create_recipe, get_recipe  # 開一個 API 接口

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup$', get_signup),  # ^ 表字首對應; $ 表字尾對應
    url(r'^signup/post$', post_signup),
    url(r'^login/post$', post_login),
    url(r'^logout/post$', post_logout),
    url(r'^api/recipes$', get_recipes_api),   # 定義一個 API 接口, 會吐回所有的 recipes 的列表
    url(r'^recipes/(\d+)$', get_recipe),   # \d: 正規表達式,代表整數, 1:# 代表一個以上的整數
    url(r'^recipes/create$', get_create_recipe),
    url(r'^recipes/create/post$', post_create_recipe),
    url(r'^', get_index)   # 進到首頁, url 網址會交由 get_index 這個 views 去處理
]
'''
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^add/(\d+)/(\d+)', get_index)
    # 利用網址帶入一些訊息, 透過 parameter 去做網址傳遞
    # 以計算機範例, 網址使用正歸表達式 https://zh.wikipedia.org/wiki/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
    # 是一種電腦科學的概念, 透過符號的方式去 mapping 字串一些意義, \d 表"符合一個數字字元。等價於[0-9]"
]
'''


