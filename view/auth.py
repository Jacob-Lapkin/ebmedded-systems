from email import message
from flask import Blueprint, request, jsonify
from  flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import generate_password_hash
from models import User, db


auth = Blueprint("auth", __name__, url_prefix="")

@auth.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        login_information = request.get_json()
        if "email" and "password" and "confirm_password" not in login_information:
            return jsonify(message="Missing information"), 400
        email = login_information['email']
        password = login_information['password']
        confirm_password = login_information['confirm_password']
        check_user = User.query.filter_by(email = email).first()
        if check_user != None:
            return jsonify(message = "Email already exists"), 400
        if password != confirm_password:
            return jsonify(message="Passwords do not match"), 400
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(message = "user created"), 201

    
    