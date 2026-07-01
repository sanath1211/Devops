from flask import Flask , request, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import json
import os
load_dotenv()

uri = os.getenv('MONGO_URL')
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.test
collection = db['flask-tutorial']
app = Flask(__name__)


@app.route("/submit", methods = ['POST'])
def submit():
    form_data = dict(request.json)      # has to be a python dict cause nosql deals with json objects

    collection.insert_one(form_data)
    return 'Data submitted successfully'

@app.route("/add-item", methods = ['POST'])
def add_item():
    form_data_to_do = dict(request.json)      # has to be a python dict cause nosql deals with json objects

    collection.insert_one(form_data_to_do)
    return 'Item added successfully'


@app.route("/view")
def view_data():
    data = collection.find()        #returns cursor
    data = list(data)          #make into python list

    for item in data:
        print(item)
        del item['_id']

    data = {
        'data' : data 
    }
    return data

@app.route("/api")
def get_data():
    with open("data.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port= 9000, debug = True)