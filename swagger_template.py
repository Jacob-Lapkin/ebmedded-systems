

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
                            "description": "Registration unsuccessful.",
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
                                        "type":"string",
                                    },
                                    "password":{
                                        "type":"string"
                                    },
                                    "confirm_password":{
                                        "type":"string"
                                    },
                                    "device":{
                                        "type":"string"
                                    },
                                }
                            },
                                "required": ["email", "password", "confirm_password", "device"] 

                        }
                    }
                }, "parameters": [
                    {
                    "name": "User",
                    "in": "body",
                    "description": "User to register",
                    "required": True,
                    "schema": {
                        "type": "object",
                        "example":"""
{
"email":"jacobglapkin@gmail.com",
"password":"asdfgh",
"confirm_password":"asdfgh",
"device":"a3xh23"
}"""                 
                        },
                    "style": "simple"
                    }
                ]
                }
            },"/login": {
                "post": {
                    "description":"User Login",
                    "responses":{
                        "200":{
                            "description":"Logged in successfully",
                            "content": {
                                "application/json": {
                                "schema": {
                                    "type": "string"
                                }
                                }
                            }
                        }, 
                        "400":{
                            "description":"Logged in unsuccessfully",
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
                                        "type":"string",
                                    },
                                    "password":{
                                        "type":"string"
                                    }
                                }
                            },
                                "required": ["email", "password"] 

                        }
                    }
                },"parameters": [
                    {
                    "name": "User",
                    "in": "body",
                    "description": "User to Login",
                    "required": True,
                    "schema": {
                        "type": "object",
                        "example":"""
{
"email":"jacobglapkin@gmail.com",
"password":"asdfgh",
}"""                 
                        },
                    "style": "simple"
                    }
                ]
                }
            }
            }
} 