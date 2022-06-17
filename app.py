from flask import Flask, jsonify, request, redirect, render_template, session
from models import mongo, userschema, usersschema, systemschema, systemsschema
from flask_jwt_extended import JWTManager
from view.auth import auth
from dotenv import load_dotenv
from flasgger import Swagger
from swagger_template import template
from view.security import security
from flask_mail import Mail, Message
import requests
import os


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = "Change this later"


#mongo db
app.config["MONGO_URI"] = f'mongodb+srv://jakethenapkin:{os.getenv("password")}@cluster0.xx87xzv.mongodb.net/my_db?retryWrites=true&w=majority'
mongo.init_app(app)

#json web token
jwt = JWTManager(app)

#blueprints
app.register_blueprint(auth)
app.register_blueprint(security)

#swagger template
swagger = Swagger(app, template=template)




# routes
@app.route("/", methods=["POST", "GET"])
def index():
    return jsonify(message = "Welcome to Alert for You. Register your device with an email to recieve timely notifications when your door opens")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")



