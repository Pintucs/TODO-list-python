from flask import Flask, jsonify, request
import mysql.connector

# connection here
cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='crud_db')
con=cnx.cursor(dictionary=True)

app = Flask(__name__)

#Home page here...     http://127.0.0.1:5000
@app.route("/")
def hello_world():
    return "<p>My Home page !</p>"

#get data from database...    http://127.0.0.1:5000/get
@app.route("/get")
def get_all_data():
    con.execute("select * from userdata")
    result=con.fetchall()
    return jsonify({'get':result})

# Add data in database...      http://127.0.0.1:5000/create
@app.route("/create",methods=["POST"])
def create_data():
    result=request.form.to_dict()
    name=result['name']
    age=result['age']
    address=result['address']
    con.execute(f"insert into userdata(name,age,address) values {name,age,address}")
    cnx.commit()
    return "object has been created" , 201

#update data from dataase...         http://127.0.0.1:5000/update
@app.route("/update",methods=['PUT'])
def updata_data():
    result=request.form.to_dict()
    name=result['name']
    age=result['age']
    address=result['address']
    id=result['id']
    con.execute(f"update userdata set name=%s, age=%s, address=%s where id=%s",(name,age,address,id))
    cnx.commit()
    return "data updated"

# delete data from database...          http://127.0.0.1:5000/delete
@app.route('/delete/<id>',methods=['DELETE'])
def delete_data(id):
    con.execute(f"delete from userdata where id={id}") 
    cnx.commit()
    return "data deleted"

if __name__ == '__main__':
   app.run(debug = True)