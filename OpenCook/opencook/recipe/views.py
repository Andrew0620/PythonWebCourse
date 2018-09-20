# API 接口

from django.shortcuts import render, redirect
from .models import Recipe
from django.http import JsonResponse   # 引入 json response 的一個套件, 可以幫助我們簡化
from django.core import serializers
from django import forms
from django.contrib import messages   # django 內建的訊息框架


# Create your views here.

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_path', 'description']
'''Django Form
1.用 HTML 建立 form 使用者介面
2.處理 HTTP POST request
3.檢查表單欄位內容是否正確
4.將確認過後的資料存進 database 當中'''


def get_recipes_api(request):
    recipes = Recipe.objects.all()
    data = serializers.serialize('json', recipes)# recipe 取出來事實上是 query set, 要進行資料轉換轉成 json 的 format, json format 是一種輕量式傳遞資料的方式
    return JsonResponse({'data': data})

'''
介紹 html, css and javascript 的時候, 有使用一個 ajax 的一個方法, 可透過 ajax 的方法, 在前端使用 javascript 去呼叫 API, 那我們 return 的 json 的 data 就可以在前端進行組件我們前端的介面, 把資料榮進 html 裡面
'''
# 單元 34
def get_recipe(request, recipe_id):     # 點選食譜縮圖可以進到詳細的食譜資料
    print(recipe_id)
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipe.html', locals())

# 單元 33
def get_create_recipe(request):
    return render(request, 'create_recipe.html')

def post_create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():  # 會和我們建立好的 model, 看我們裡面有沒有設一些預設的條件
             new_recipe = form.save()
             print(new_recipe)
             messages.add_message(request, messages.SUCCESS, '分享成功！')
             return redirect('/', locals())
        else:
             return redirect('/recipe/create')

