from flask import Flask, render_template, redirect, url_for, request, session
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'requestMachineDB'
app.config['MONGO_URI'] = 'mongodb+srv://dbAdmin:7sohc2fjtQp4kEgY@myfirstcluster-ji3yz.mongodb.net/requestMachineDB?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/find_config')
def find_config():
    return render_template("findconfig.html")


@app.route('/get_laptops')
def get_laptops():
    return render_template("laptops.html", Laptops=mongo.db.laptops.find())



@app.route('/get_softwares')
def get_softwares():
    return render_template("softwares.html", Softwares=mongo.db.softwares.find())



@app.route('/add_laptop')
def add_laptop():
    return render_template("addlaptop.html")



@app.route('/add_software')
def add_software():
    return render_template("addsoftware.html")



@app.route('/edit_laptops')
def edit_laptops():
    return render_template("editlaptops.html", Laptops=mongo.db.laptops.find())


@app.route('/edit_softwares')
def edit_softwares():
    return render_template("editsoftwares.html", Softwares=mongo.db.softwares.find())
    

@app.route('/insert_laptop', methods=['POST'])
def insert_laptop():
    Laptops = mongo.db.laptops
    Laptops.insert_one(request.form.to_dict())
    return redirect(url_for('get_laptops'))


@app.route('/insert_software', methods=['POST'])
def insert_software():
    mongo.db.softwares.insert_one(request.form.to_dict())
    return redirect(url_for('get_softwares'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
