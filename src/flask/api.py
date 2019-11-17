#!/usr/bin/python3
# api.py

import os
from flask import Flask, jsonify, redirect, request, render_template, url_for


app = Flask(__name__, template_folder="templates")
app.config.from_object("config")


# Home
@app.route(app.config["HOME"], methods=["GET"])
def get_home():
    versions = list(map(lambda x: str(x), app.config["VERSIONS"]))[::-1]
    return render_template("home.html", title=app.config["API_NAME"] + " | Home", versions=versions, API_NAME=app.config["API_NAME"])


# Error handlers
@app.errorhandler(404)
def error_404(e):
    return render_template("404.html"), 404


@app.errorhandler(400)
def error_400(e):
    return "HTTP 400 - Bad Request", 400


@app.errorhandler(500)
def error_500(e):
    return "HTTP 500 - Internal Server Error", 500


# API Endpoints
# Version 1.0
@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0"), methods=["GET"])
def get_endpoint_1_0():
    return "Welcome to version 1.0 of the " + app.config["API_NAME"] + " API!"\
           "<br>This API is currently under development, and is not intended for stable use."


# API Docs
# Version 1.0
@app.route(os.path.join("/", app.config["API_NAME"].lower(), "docs", "v1.0"), methods=["GET"])
def get_docs_1_0():
    content = [
        {
            "title": "Generate Token",
            "description": "Lorem ipsum dolor sit amet, <code>consectetur</code> adipiscing elit. Quisque nec venenatis est. Aliquam scelerisque bibendum volutpat. Donec vehicula tincidunt arcu, nec pellentesque neque dignissim eu. Duis a pretium sapien. Suspendisse efficitur eu metus ultrices suscipit. Mauris eget nulla a urna fermentum vulputate. Fusce ac leo rhoncus, convallis sem vel, blandit velit. Vestibulum pharetra dapibus nisi fermentum pretium.",
            "request": [
                {
                    "parameter": "authorization",
                    "type": "string",
                    "position": "header",
                    "required": "yes",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                },
                {
                    "parameter": "username",
                    "type": "string",
                    "position": "body",
                    "required": "yes",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nec venenatis est. Aliquam scelerisque bibendum volutpat. Donec vehicula tincidunt arcu, nec pellentesque neque dignissim eu."
                }
            ],
            "response": """{
    "status": true,
    "result_code": 200,
    "message": "Success!",
    "values": {
        "name": "Kiddy",
        "email": "kiddydhana@gmail.com",
        "token": "9WUzKE7kCI1vSuQAbrmOwc2m2dk1NbPR",
        "account_status": "1"
    }
}"""
        }
    ]
    return render_template("docs.html", API_NAME=app.config["API_NAME"], content=content)


if __name__ == "__main__":
    app.run(app.config["IP"], app.config["PORT"])
