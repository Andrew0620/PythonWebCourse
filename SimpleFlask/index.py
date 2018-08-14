from flask import Flask, render_template    #Flask 的類別主要是接收套件或模組的名稱當作參數
app = Flask(__name__)     #如果程式自己執行的話, name=__name__, 如果不是,則傳進套件或模組的名稱
# 希望讓 Flask 的程式知道說, 怎麼把你的模板 template 和 static 靜態檔案目錄的一個相對位子

@app.route('/hello')
def hello():
    return 'hello world!!'

@app.route('/')   #當妳進到首頁會做什麼事
def index():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(port=9000)   #TCP/UDP 阜列表, port 對應不同通訊協定的服務