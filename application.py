import json
from flask import Flask, jsonify, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from flask_cors import cross_origin

application = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:root@localhost:3306/pronounce"
application.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://lakal:lakal123@aa1p3em59w94kxc.cbc3zkb8fpux.us-east-2.rds.amazonaws.com:3306/ebdb"
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(application)


@dataclass()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"['email=>{self.email}, password=>{self.password}']"


db.create_all()
db.session.commit()

@application.route('/')
def index():
    return "Welcome to Pronounce"


@application.route('/login', methods=['POST'])
@cross_origin()
def loginRoute():
    global response
    if request.method == "POST":
        request_data = json.loads(request.data)
        email = request_data["email"]
        password = request_data["password"]
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return "Success"


if __name__ == "__main__":
    application.run(debug=True)
