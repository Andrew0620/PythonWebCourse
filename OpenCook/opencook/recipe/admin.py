from django.contrib import admin
from recipe.models import Recipe

# Register your models here.
'''
單元27: Django 會員管理系統 admin(後臺操作)
圖形化介面去操作我們的資料庫和管理我們的權限
Django 有一個 admin 的後台管理系統
'''
# 需作一些設定才能讓 recipe 出現在後台
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Recipe, RecipeAdmin)    # 綁定 admin, 並把 Recipe 註冊進去