from email import message
from venv import create
from flask import Blueprint, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from models import mongo, userschema, usersschema
from bson import json_util


auth = Blueprint("auth", __name__, url_prefix="")

@auth.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        print("requested")
        login_information = request.get_json()
        if "email" not in login_information.keys() or "password" not in login_information.keys() or "confirm_password" not in login_information.keys() or 'device'not in login_information.keys():
            return jsonify(message="Missing information"), 400
        email = login_information['email']
        password = login_information['password']
        confirm_password = login_information['confirm_password']
        device = login_information['device']
        check_device = mongo.db.systems.find_one({'device':device})
        check_user = mongo.db.user.find_one({"email":email})
        try:
            system_id = json_util.dumps(check_device["_id"])
        except TypeError:
            return jsonify(message = "This device does not exist"), 400
        check_device_exist = mongo.db.user.find_one({"system_id":system_id})
        if check_device_exist != None:
            return jsonify(message = "This device has already been registered"), 400
        if check_user != None:
            return jsonify(message = "Email already exists"), 400
        if password != confirm_password:
            return jsonify(message="Passwords do not match"), 400
        hashed_password = generate_password_hash(password)
        try:
            loaded_user = userschema.load({"email": email, "password":hashed_password, "system_id":system_id})
        except ValidationError:
            return jsonify(message="Did not supply correct data types"), 400
        new_user = mongo.db.user.insert_one(loaded_user)
        return jsonify(message = "user created"), 201

@auth.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        login_data = request.get_json()
        if "email" not in login_data.keys() or "password" not in login_data.keys():
            return jsonify(message = "missing information"), 400
        email = login_data["email"]
        password = login_data['password']
        find_user = mongo.db.user.find_one({"email":email})
        if not find_user:
            return jsonify(message = "email does not exist"), 400
        
        check_password = check_password_hash(find_user['password'], password)
        print(find_user['password'])
        if not check_password:
            return jsonify(message = "password does not match"), 400
        token = create_access_token(identity= email)
        return jsonify(message = "Logged in successfully", access_token = token), 200


    
    