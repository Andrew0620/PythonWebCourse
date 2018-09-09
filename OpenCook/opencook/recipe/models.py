from django.db import models
from django.utils import timezone    # 希望引入現在創建時間
# Create your models here.

'''
單元 26 Model schema 建置, 去建置我們要的資料表
Django 預設會為每一個 model 加上 id 欄位, 並將此欄位設成 primary key(pk), 這樣一來每筆資料都有著獨一無二的 id
'''
class Recipe(models.Model):   # 宣告類別
    title = models.CharField(max_length=100)         # 資料型態: CharField (食譜標題)
    image_path = models.CharField(max_length=100)    # 資料型態: CharField (照片網址)
    description = models.TextField()                  # 資料型態: TextField (食譜描述)
    crated_at = models.DateTimeField(default=timezone.now)      # 資料型態: DateTimeField (創建時間)

'''
使用 django model 指令去建造我們的 model 去產生出來
1. python manage.py makemigrations 依照 model 的修改, 刪除, 建立一個新的 migration(遷移) 紀錄檔案, 繼魯你去修改 model 的過程,把它紀錄成一個檔案
2. python manage.py migrate 更新資料庫中的資料表: 對應到資料庫, 透過 migrate 的方式, 把 migration 的紀錄檔依照我們更新資料, 去對應到我們真正的資料庫要進行怎樣的更新
3. python manage.py shell 在指令環境下操作 QuerySet API: 可進入互動式指令碼的環境下去存取和操作我們的資料
ps. 須注意在 opencook/seetings.py 的 INSTALLED_APPS =[] 有無新增 'mainapp' 和 'recipe'
'''