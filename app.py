from flask import Flask, jsonify, request, redirect, render_template, session
from models import db, System, User
from flask_jwt_extended import JWTManager
from view.auth import auth

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///embedded.db'
app.config['SECRET_KEY'] = "Change this later"

db.init_app(app)

jwt = JWTManager()

#blueprints
app.register_blueprint(auth)


# functions for db
def create_db():
    with app.app_context():
        db.create_all()

def drop_db():
    with app.app_context():
        db.drop_all()


def seed_db():
    with app.app_context():
        walle = System(device = "4xd6sg")
        db.session.add(walle)
        db.session.commit()
        print("seeded database")


# routes
@app.route("/", methods=["POST", "GET"])
def index():
    return jsonify(message = "This is a test"), 200

if __name__ == "__main__":
    app.run(debug=True)



