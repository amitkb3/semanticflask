from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/concept')
def concept():
  # data = { "image":"lion.jpg","english":"Lion","hindi":"सिंह"}
  data = { "image":"parrot_small_640px.jpg","english":"Parrot","hindi":"तोता"}
  return render_template('concept.html', data=data)
