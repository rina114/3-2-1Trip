# インストールした「flask」モジュールをインポートする
import os
from flask import (
    Flask, 
    request, 
    render_template)
from model import word_get

# インスタンス化する
app = Flask(__name__) #アンダースコア(_)をnameの左右にそれぞれ2つずつ書く

#ルーティング設定をする
# スタート画面
@app.route('/', )
def index():
    return render_template('index.html')

#アプリの概要
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

# 入力画面
@app.route('/input', methods=['GET', 'POST'])
def data_input():
    return render_template('input.html')

# 結果表示画面
@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        word_1 = request.form['word_1']
        word_2 = request.form['word_2']
        word_3 = request.form['word_3']
        n_num = request.form['radio1']
        if n_num == '１～２人':
            num = 0
        else:
            num = 1
        n_point = request.form['radio2']
        if n_point == '景色':
            point = 0
        else:
            point = 1
        n_popularity = request.form['radio3']
        if n_popularity == '定番':
            popularity = 0
        else:
            popularity = 1
        url, name, caption, address, img_path, around_url = word_get(word_1, word_2, word_3, num, point, popularity)
    return render_template('result.html', url=url, name=name, caption=caption, address=address, img_path=img_path, around_url=around_url)

if __name__ == "__main__": #最後に記述する
    app.run(debug=True)