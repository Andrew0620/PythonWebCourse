import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('SimpleDB.sqlite')  # 連結資料庫 SimpleDB

cursor = conn.cursor()  # cursor 可以幫助我們新增, 刪除, 修改資料內容

sqlstr = 'INSERT INTO user ("id", "username") VALUES ("1", "Leo")'

cursor.execute(sqlstr)   # 執行

conn.commit()   # 提交

conn.close()
