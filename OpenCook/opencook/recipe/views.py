# API 接口

from django.shortcuts import render
from .models import Recipe
from django.http import JsonResponse   # 引入 json response 的一個套件, 可以幫助我們簡化
from django.core import serializers
# Create your views here.

def get_recipes_api(request):
    recipes = Recipe.objects.all()
    data = serializers.serialize('json', recipes)# recipe 取出來事實上是 query set, 要進行資料轉換轉成 json 的 format, json format 是一種輕量式傳遞資料的方式
    return JsonResponse({'data': data})

'''
介紹 html, css and javascript 的時候, 有使用一個 ajax 的一個方法, 可透過 ajax 的方法, 在前端使用 javascript 去呼叫 API, 那我們 return 的 json 的 data 就可以在前端進行組件我們前端的介面, 把資料榮進 html 裡面
'''
