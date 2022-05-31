from flask import Flask, jsonify, request, redirect, render_template, session
from models import mongo, userschema, usersschema
from flask_jwt_extended import JWTManager
from view.auth import auth
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = "Change this later"
app.config["MONGO_URI"] = f'mongodb+srv://jakethenapkin:{os.getenv("password")}@cluster0.xx87xzv.mongodb.net/my_db?retryWrites=true&w=majority'


mongo.init_app(app)

jwt = JWTManager()

#blueprints
app.register_blueprint(auth)


# routes
@app.route("/", methods=["POST", "GET"])
def index():
    find_this = {"device":"4xd6sg"}
    device = mongo.db.systems.find_one(find_this)
    return jsonify(message = device), 200

if __name__ == "__main__":
    app.run(debug=True)



