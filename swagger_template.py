

template ={
    "openpai": "3.0.3",
    "info":{
                "title":"Embedded Systems API",
                "description": "Building a very good api for embedded systems",
                "contact": {
                "name":"Jacob Lapkin",
                "email":"jacobglapkin@gmail.com"
            },
            "version": "v1"
            },
    "servers": {
                "url":"http://localhost:5000/",
                "description":"Development server"
            },
    "paths":{
            "/register":{
                "post":{
                    "description":"Registers a new user that has a device",
                    "responses":{
                        "201":{
                            "description": "Registration successful.",
                            "content": {
                                "application/json": {
                                "schema": {
                                    "type": "string"
                                }
                                }
                            }
                        },
                        "400":{
                            "description": "Registration unsuccesful.",
                            "content": {
                                "application/json": {
                                "schema": {
                                    "type": "string"
                                }
                                }
                            }
                        }
                    },"requestBody": {
                    "content": {
                        "application/json":{
                            "schema":{
                                "type":"object",
                                "properties":{
                                    "email":{
                                        "type":"string"
                                    },
                                    "password":{
                                        "type":"string"
                                    },
                                    "confirm_password":{
                                        "type":"string"
                                    },
                                    "device":{
                                        "type":"string"
                                    }
                                }
                            },
                                "required": ["email", "password", "confirm_password", "device"] 

                        }
                    }
                }, "parameters": [
                    {
                    "name": "email",
                    "in": "path",
                    "description": "email address to register",
                    "required": True,
                    "schema": {
                        "type": "string"
                    },
                    "style": "simple"
                    },
                    {
                    "name": "password",
                    "in": "path",
                    "description": "password to register",
                    "required": True,
                    "schema": {
                        "type": "string"
                    },
                    "style": "simple"
                    },
                    {
                    "name": "confirm_password",
                    "in": "path",
                    "description": "confirm your password",
                    "required": True,
                    "schema": {
                        "type": "string"
                    },
                    "style": "simple"
                    },
                    {
                    "name": "device",
                    "in": "path",
                    "description": "This is the code that comes with your device",
                    "required": True,
                    "schema": {
                        "type": "string"
                    },
                    "style": "simple"
                    }
                ]
                }
            }
            }
} 