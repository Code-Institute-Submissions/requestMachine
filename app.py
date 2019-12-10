from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'requestMachineDB'
app.config['MONGO_URI'] = 'mongodb+srv://dbAdmin:7sohc2fjtQp4kEgY@myfirstcluster-ji3yz.mongodb.net/requestMachineDB?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_laptops')
def get_laptops():
    return render_template("laptops.html", Laptops=mongo.db.laptops.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
