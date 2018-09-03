import cv2
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])  # 處理網址列的部分
def upload():
    if request.method == 'POST':
        file = request.files['img']

        file.save('./' + file.filename)

        cascPath = 'haarcascade_frontalface_default.xml'

        faceCascade = cv2.CascadeClassifier(cascPath)  # 把特徵值吃進來

        image = cv2.imread(file.filename)   # 把 img 吃進來, imr=read image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 把圖片從 BGR 轉成 gray

        return render_template('index.html')

if __name__ == '__main__':
    app.run()