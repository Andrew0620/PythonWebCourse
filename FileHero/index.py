import os

filename = 'hello_word.txt'

if os.path.exists(filename):
    os.remove(filename)  #如果有 hello_world.txt 這個資料, 就移進去

else:
    with open(filename, 'w') as f:    #沒有就新增檔案, 用 with; w=write, r=read, a=append
        f.write('Hello World!!!')

