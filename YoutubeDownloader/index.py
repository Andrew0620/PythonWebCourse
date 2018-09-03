from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    filename = request.args.get('filename')
    print(filename)
    return render_template('index.html', filename=filename)

@app.route('/submit', methods=['POST'])
def post_submit():
    #yt = YouTube()
    url = request.form.get('url')
    default_filename = YouTube(url).streams.first().default_filename
    #YouTube(url).streams.first().download()
    #yt.url = url
    #video = yt.get('mp4', '360p')
    #video.download('./')
    #filename = yt.filename
    #print(yt)
    #print(yt.filname)
    return redirect(url_for('index', filename=default_filename)) #回跳到首頁, 把當做參數在上傳成功時帶過去




if __name__ == '__main__':
    app.run(debug=True)
