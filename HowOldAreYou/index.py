import cv2
from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    filename = request.args.get('filename')
    result = request.args.get('result')
    return render_template('index.html', filename = filename, result = result)

@app.route('/upload', methods=['POST'])  # 處理網址列的部分
def upload():
    if request.method == 'POST':
        file = request.files['img']

        file.save('./' + file.filename)

        cascPath = 'haarcascade_frontalface_default.xml'

        faceCascade = cv2.CascadeClassifier(cascPath)  # 把特徵值吃進來

        image = cv2.imread(file.filename)   # 把 img 吃進來, imreadr=read image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 把圖片從 BGR 轉成 gray(灰階的圖片)

        faces=faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        # faceCascade.detectMultiScale 辨識人臉的方法;
        # scaleFactor=1 依據不同大小去對圖片進行掃描特徵比對, 所謂的膨脹係數膨脹係數越大越精確
        #  minNeighbors 控制檢驗的誤差參數, 5 代表 5 個區塊, 特徵比對正確才判斷有人臉, 數字越大越嚴謹, 預設值為 3
        # minSize 每次去辨識區塊的大小是怎樣
        # flags 檢測的模式, 使用的是 cv2 裡面的預設, 使用 cv2.CASCADE_SCALE_IMAGE 去辨識

        for (x, y, w, h) in faces:
            age = random.randint(18, 30)  # 年齡設定範圍
            cv2.rectangle(image, (x + 3, y - 15), (x + 50, y - 50), (200, 187, -1), -1) 　
            # 放年齡文字的地方
            cv2.putText(image, str(age), (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0, 187), 2)
            # 塞進年齡, cv2.FONT_HERSHEY_SIMPLEX 字體形式
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite('./static/images/' + file.filename, image)  # cv2.imwrite 保存图像
        # 用 for loop 把人臉辨識範圍用矩形表示出來
        # cv2.rectangle: img是原图, （x，y）是矩阵的左上点坐标, (x+w，y+h）是矩阵的右下点坐标,
        # （0,255,0）是画线对应的 rgb 颜色, 2 是所画的线的宽度(-1表實心)
        #  cv2.imwrite: 第一个参数是文件名，第二个参数是你要保存的图片，
        # 第三个参数针对特定的格式： 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95
        newImage = './static/images/' + file.filename

        return redirect(url_for('index', filename = newImage, result = len(faces)))
        # 重新定向到 index 的地方, 帶出檔名, result 看是否辨識出人臉: 0 代表 fail

        return render_template('index.html')

if __name__ == '__main__':
    app.run()