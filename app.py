from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/concept')
def concept():
  data = { "image":"lion.jpg","english":"Lion","hindi":"सिंह"}
  return render_template('concept.html', data=data)
