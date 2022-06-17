from models import mongo 
from flask import request, jsonify, Blueprint
from bson import json_util
from flask_jwt_extended import get_jwt_identity, jwt_required
from datetime import datetime 
import requests
from datetime import datetime
from dotenv import load_dotenv
import os
from twilio.rest import Client
load_dotenv()


security = Blueprint("security", __name__, url_prefix="")

# get current time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

def send_mail(recipient):
    """ takes in recipient to email, sends alert email to recipient"""

    requests.post(
		"https://api.mailgun.net/v3/sandbox5190a0e2f6034bd08ccf185a2d8c52e1.mailgun.org/messages",
		auth=("api", f'{os.getenv("mail_key")}'),
		data={"from": "AFY mailgun@sandbox5190a0e2f6034bd08ccf185a2d8c52e1.mailgun.org",
			"to": [f'{recipient}'],
			"subject": "New Security Alert",
			"text": f'Please be aware that your door has been opened at {dt_string}. We recommend checking with who is home or call 911'})

def send_text(recipient):
    """Takes in recipient phone number, sends alert text to recipient"""
    account_sid = f'{os.getenv("twilio_account_sid")}' 
    auth_token = f'{os.getenv("twilio_auth_token")}' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create(  
                              messaging_service_sid='MGb2dea8244047e95480134d52fba21c5c', 
                              body=f'Your door has opened at {dt_string}',      
                              to=f'+{recipient}' 
                          ) 
    print(message.sid)


@security.route("/alert", methods=["POST", "GET"])
def get_message():
    if request.method == "POST":
        data = request.get_json()
        for key, value in data.items():
            if key != "device":
                return jsonify(message="Incorrect arguments"), 400
        device = data['device']
        check_device = mongo.db.systems.find_one({"device":device})
        if check_device == None:
            return jsonify(message ="Device does not exist"), 400
        system_id = json_util.dumps(check_device["_id"])
        user = mongo.db.user.find_one({"system_id":system_id})
        if not user:
            return jsonify(message="device has not been registered to user")
        dump_user = json_util.dumps(user["_id"])
        new_alert = {"user_id":dump_user, "date":str(datetime.now().date())}
        mongo.db.alerts.insert_one(new_alert)
        send_mail(user['email'])
        send_text(user['phone'])
        return jsonify(message = "Inserted alert and sent alert"), 200
  
        

