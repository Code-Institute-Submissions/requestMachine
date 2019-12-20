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
    return render_template("findconfig.html", Laptops=mongo.db.laptops.find(), Softwares=mongo.db.softwares.find())


@app.route('/add_software_to_mysoftwares/<software_id>')
def add_software_to_mysoftwares(software_id):
    software=mongo.db.softwares.find({"_id":ObjectId(software_id)})
    mongo.db.softwares.update({"_id":ObjectId(software_id)},
        {
        
        'software_name':software.software_name,
        'produced_by':software.produced_by,
        'proc_gen': software.proc_gen,
        'proc_cores': software.proc_cores,
        'proc_min':software.proc_min,
        'ram_size':software.ram_size,
        'hard_drive':software.hard_drive,
        'gpu_ram':software.gpu_ram,
        'img_source':software.img_source,
        'chosen':True
    })
    return render_template("findconfig.html", Laptops=mongo.db.laptops.find(), Softwares=mongo.db.softwares.find())



@app.route('/remove_software_from_mysoftwares/<software_id>')
def remove_software_from_mysoftwares(software_id):
    software=mongo.db.softwares.find({"_id":ObjectId(software_id)})
    mongo.db.softwares.update({"_id":ObjectId(software_id)},
        {
        
        'software_name':software.software_name,
        'produced_by':software.produced_by,
        'proc_gen': software.proc_gen,
        'proc_cores': software.proc_cores,
        'proc_min':software.proc_min,
        'ram_size':software.ram_size,
        'hard_drive':software.hard_drive,
        'gpu_ram':software.gpu_ram,
        'img_source':software.img_source,
        'chosen':False
    })
    return render_template("findconfig.html", Laptops=mongo.db.laptops.find(), Softwares=mongo.db.softwares.find())




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
    return redirect(url_for('edit_laptops'))


@app.route('/insert_software', methods=['POST'])
def insert_software():
    mongo.db.softwares.insert_one(request.form.to_dict())
    return redirect(url_for('edit_softwares'))



@app.route('/edit_laptop/<laptop_id>')
def edit_laptop(laptop_id):
    return render_template('updatelaptop.html', laptop=mongo.db.laptops.find_one({"_id": ObjectId(laptop_id)}))



@app.route('/update_laptop/<laptop_id>', methods=["POST"])
def update_laptop(laptop_id):
    mongo.db.laptops.update( {"_id": ObjectId(laptop_id)},
    {
        
        'model_name':request.form.get('model_name'),
        'model_number':request.form.get('model_number'),
        'proc_gen': request.form.get('proc_gen'),
        'proc_cores': request.form.get('proc_cores'),
        'proc_max':request.form.get('proc_max'),
        'ram_size':request.form.get('ram_size'),
        'hard_drive':request.form.get('hard_drive'),
        'gpu_ram':request.form.get('gpu_ram'),
        'img_source':request.form.get('img_source')
    })
    return redirect(url_for('edit_laptops'))


@app.route('/delete_laptop/<laptop_id>)')
def delete_laptop(laptop_id):
    mongo.db.laptops.remove( {"_id": ObjectId(laptop_id)})
    return redirect(url_for('edit_laptops'))


@app.route('/edit_software/<software_id>')
def edit_software(software_id):
    return render_template('updatesoftware.html', software=mongo.db.softwares.find_one({"_id": ObjectId(software_id)}))



@app.route('/update_software/<software_id>', methods=["POST"])
def update_software(software_id):
    mongo.db.software.update( {"_id": ObjectId(software_id)},
    {
        
        'software_name':request.form.get('software_name'),
        'produced_by':request.form.get('produced_by'),
        'proc_gen': request.form.get('proc_gen'),
        'proc_cores': request.form.get('proc_cores'),
        'proc_min':request.form.get('proc_min'),
        'ram_size':request.form.get('ram_size'),
        'hard_drive':request.form.get('hard_drive'),
        'gpu_ram':request.form.get('gpu_ram'),
        'img_source':request.form.get('img_source')
    })
    return redirect(url_for('edit_softwares'))


@app.route('/delete_software/<software_id>)')
def delete_software(software_id):
    mongo.db.softwares.remove( {"_id": ObjectId(software_id)})
    return redirect(url_for('edit_softwares'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', '5000')),
            debug=True)
