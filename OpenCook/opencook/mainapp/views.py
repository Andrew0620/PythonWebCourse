# view 為商業邏輯撰寫的一個部分

from django.shortcuts import render
form django.http import HttpResponse

# Create your views here.

def get_index(request):
    return HttpResponse('Hello World!')
