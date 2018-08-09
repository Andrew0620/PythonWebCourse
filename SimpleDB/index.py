import sqlite3

conn = sqlite3.connect('SimpleDB.sqlite')  # 連結資料庫 SimpleDB

cursor = conn.cursor()  # cursor 可以幫助我們新增, 刪除, 修改資料內容

sqlstr = 'INSERT INTO user ("id", "username") VALUES ("1", "Leo")'

'''
cursor.execute(sqlstr)   # 執行
'''
'''
cursor = conn.execute('SELECT * FROM user')  # 執行宣告多個變數
'''
rows = cursor.fetchall()    # 執行一個 function 較 fetchall

cursor = conn.execute('UPDATE user SET username="Jack" WHERE username="Leo"')
# 更新資料做法 Jack 取代 Leo

print(rows)

conn.commit()   # 提交

conn.close()
