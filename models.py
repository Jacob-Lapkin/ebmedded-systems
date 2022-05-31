from flask_pymongo import PyMongo
from marshmallow import Schema, fields

mongo = PyMongo()

class UserSchema(Schema):
    _id = fields.Str()
    email = fields.Email()
    phone = fields.Int()
    password = fields.Str()

class SystemSchema(Schema):
    _id = fields.Str()
    device = fields.Str()

usersschema = UserSchema(many = True)
userschema = UserSchema()

systemsschema = SystemSchema(many = True)
systemschema = SystemSchema()



