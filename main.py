from logging import debug
from flask import Flask,jsonify,request,jsonify, make_response
import json
from flask_sqlalchemy import SQLAlchemy
from dataclasses import  dataclass

from werkzeug.wrappers import response

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=""
db = SQLAlchemy(app)

@dataclass()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120),nullable=False)
    password= db.Column(db.String(80),nullable=False)

    def __init__(self,email,password):
        self.email=email
        self.password=password

    def __repr__(self):
        return f"['email=>{self.email}, password=>{self.password}']"
    
db.create_all()
db.session.commit()

@app.route('/name',method = ['GET', 'POST'])
def nameRoute():

    global response

    if(request.method == 'POST'):
        request_data = json.loads(request.data)
        email = request_data['email']
        password = request_data['password']
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return "Success"

if __name__ == '__main__':
    app.run(debug=True, host='' , port=800)