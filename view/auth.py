from email import message
from flask import Blueprint, request, jsonify
from  flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash
from models import mongo, userschema, usersschema


auth = Blueprint("auth", __name__, url_prefix="")

@auth.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        login_information = request.get_json()
        if "email" not in login_information.keys() or "password" not in login_information.keys() or "confirm_password" not in login_information.keys() or 'device'not in login_information.keys():
            return jsonify(message="Missing information"), 400
        email = login_information['email']
        password = login_information['password']
        confirm_password = login_information['confirm_password']
        device = login_information['device']
        check_device = mongo.db.systems.find_one({'device':device})
        check_user = mongo.db.user.find_one({"email":email})

        check_device_exist = mongo.db.user.find_one({"system_id":check_device['_id']})
        if not check_device_exist:
            return jsonify(message = "This device does not exist"), 400
        if check_device_exist != None:
            return jsonify(message = "This device has already been registered"), 400
        if check_user != None:
            return jsonify(message = "Email already exists"), 400
        if password != confirm_password:
            return jsonify(message="Passwords do not match"), 400
        hashed_password = generate_password_hash(password)
        new_user
        new_user = mongo.db.user.insert_one({"email": email, "password":hashed_password, "system_id":check_device['_id']})
        return jsonify(message = "user created"), 201

    
    