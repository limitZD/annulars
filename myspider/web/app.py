from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def lagou():
    return render_template('lagou/index.html')

@app.route('/index')
def lianjia():
    return render_template('lianjia/index.html')


@app.route('/index')
def dianping():
    return render_template('dianping/index.html')

if __name__ == '__main__':
    app.run()
