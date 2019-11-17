#!/usr/bin/python3
# api.py

import os
import sys
sys.path.append(os.path.abspath(__file__).split("/flask/")[-2])
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


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "graph", "<string:type>"), methods=["GET"])
def get_graph_url():
    return url_for("static", filename="graphs/weekly.png")


# API Docs
# Version 1.0
@app.route(os.path.join("/", app.config["API_NAME"].lower(), "docs", "v1.0"), methods=["GET"])
def get_docs_1_0():
    content = [
        {
            "title": "Get graph URL",
            "request_type": "GET",
            "url": os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "graph", "<string:type>"),
            "description": "Retrieve the URL for the specified graph type.",
            "request": [
                {
                    "parameter": "type",
                    "type": "string",
                    "position": "header",
                    "required": "yes",
                    "description": "Type of graph to retrieve, options are 'weekly' and 'total'"
                }
            ],
            "response": "http://" + app.config["IP"] + ":" + str(app.config["PORT"]) + "/static/graphs/graph.png"
        }
    ]
    return render_template("docs.html", API_NAME=app.config["API_NAME"], content=content)


if __name__ == "__main__":
    app.run(app.config["IP"], app.config["PORT"])
