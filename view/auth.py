from email import message
from flask import Blueprint, request, jsonify
from  flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash
from models import db, System, User


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
        check_user = User.query.filter_by(email = email).first()
        check_device = System.query.filter_by(device = device).first()
        try:
            check_device_exist = User.query.filter_by(system_id = check_device.id).first()
        except AttributeError:
            return jsonify(message = "This device does not exist"), 400
        if check_device_exist != None:
            return jsonify(message = "This device has already been registered"), 400
        if check_user != None:
            return jsonify(message = "Email already exists"), 400
        if password != confirm_password:
            return jsonify(message="Passwords do not match"), 400
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password, system_id = check_device.id)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message = "user created"), 201

    
    