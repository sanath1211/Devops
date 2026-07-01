from flask import Flask , render_template, request
import requests

BACKEND_URL = 'http://127.0.0.1:9000/' 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/to-do")
def to_do():
    return render_template('to-do.html')

@app.route("/submit", methods = ['POST'])
def submit():
    form_data = dict(request.form)

    requests.post(BACKEND_URL + '/submit', json = form_data)

    return 'Data Submitted'

@app.route("/add-item", methods = ['POST'])
def add_item():
    form_data_to_do = dict(request.form)

    requests.post(BACKEND_URL + '/add-item', json = form_data_to_do)

    return 'Item Added'

@app.route("/get-data")
def get_data():

    data = requests.get(BACKEND_URL + '/view')

    return data.json()

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 8000, debug = True)