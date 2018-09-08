from django.db import models
from django.utils import timezone    # 希望引入現在創建時間
# Create your models here.

'''
單元 26 Model schema 建置
Django 預設會為每一個 model 加上 id 欄位, 並將此欄位設成 primary key(pk), 這樣一來每筆資料都有著獨一無二的 id
'''
Class Recipe(models.Model):
    title = models.chartField(max_length=100)
    image_path = models.chartField(max_length=100)
    description = models.textField()
    crated_at = models.DateTimeFielda(default=timezone.now)
