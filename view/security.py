from models import mongo 
from flask import request, jsonify, Blueprint
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required

security = Blueprint("security", __name__, url_prefix="")

@security.route("/security", methods=["GET"])
def get_message():
    pass
