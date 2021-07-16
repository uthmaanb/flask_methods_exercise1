from flask import *
from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def shopping():
    return render_template('list.html')


@app.route('/item_list', methods=['POST', 'GET'])
def item_list():
    if request.method == 'POST':
        result = request.form
        return render_template('homepage.html', result=result)


if __name__ == '__main__':
    app.debug = True
    app.run()
