from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    filename = request.args.get('filename')
    return render_template('index.html', filename=filename)

@app.route('/submit', methods=['POST'])
def post_submit():
    yt = YouTube()
    url = request.form.get('url')
    yt.url = url
    video = yt.get('mp4', '360p')
    video.download('./')
    filename = yt.filename
    print(yt)
    print(yt.filname)
    return redirect(url_for('index', filename=filename)) #回跳到首頁

if __name__ == '__main__':
    app.run(debug=True)
