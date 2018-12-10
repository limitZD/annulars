from flask import Flask, render_template, Response
from myspider.analysis import job_analysis

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lagou')
def lagou():
    return render_template('lagou/index.html')

@app.route('/lagou/top_city')
def top_city():
    return render_template('lagou/top_city.html')

@app.route('/lagou/top_city.png')
def top_city_png():
    return Response(job_analysis.top_city_plot(format='png'),content_type='image/png')

@app.route('/index')
def lianjia():
    return render_template('lianjia/index.html')


@app.route('/index')
def dianping():
    return render_template('dianping/index.html')

if __name__ == '__main__':
    app.run()
