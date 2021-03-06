#!/usr/bin/python3
# api.py

import os
import sys
sys.path.append(os.path.abspath(__file__).split("/flask/")[-2])
from data import data
from data.recommendations import recommendations
from data.savings import savings
from flask import Flask, jsonify, redirect, request, render_template, url_for
from datetime import datetime


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
def get_graph_url(type):
    if type == "weekly":
        today = data.get_day(datetime.now().timestamp())
        this_week = [data.total_day_water(app.config["DB_FILE"], "user", datetime.fromtimestamp(datetime.now().timestamp() - 86400 * (today - d)).date()) for d in range(0, today + 1)]
        last_week = [data.total_day_water(app.config["DB_FILE"], "user", datetime.fromtimestamp(datetime.now().timestamp() - 86400 * (today - d + 7)).date()) for d in range(0, today + 1)]
        data.weekly_graph(last_week, this_week)
        return jsonify({"uri": "http://" + app.config["PRIVATE_IP"] + url_for("static", filename="graphs/weekly.png")})
    elif type == "total":
        total = data.total_weeks_water(app.config["DB_FILE"], "user")
        data.total_graph(total)
        return jsonify({"uri": "http://" + app.config["PRIVATE_IP"] + url_for("static", filename="graphs/total.png")})
    else:
        return ""


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "total", "<string:period>"), methods=["GET"])
def get_total_water(period):
    if period == "weekly":
        return data.total_week_water(app.config["DB_FILE"], "user", datetime.now().timestamp())
    elif period == "total":
        return data.total_water(app.config["DB_FILE"], "user")
    else:
        return None


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "average", "<string:period>"), methods=["GET"])
def get_average_water(period):
    if period == "weekly":
        return data.total_week_water(app.config["DB_FILE"], "user", datetime.now().timestamp()) / 7
    elif period == "total":
        return data.total_water(app.config["DB_FILE"], "user") / len(data.total_weeks_water(app.config["DB_FILE"], "user"))
    else:
        return None


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "recommendations"), methods=["GET"])
def get_recommendations():
    return jsonify(recommendations(data.highest_source(app.config["DB_FILE"], "user")))


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "highest_source"), methods=["GET"])
def get_highest_source():
    return jsonify({"source": data.highest_source(app.config["DB_FILE"], "user")})


@app.route(os.path.join("/", app.config["API_NAME"].lower(), "api", "v1.0", "savings"), methods=["GET"])
def get_savings():
    saved = round(savings(data.total_week_water(app.config["DB_FILE"], "user", datetime.now().timestamp() - 604800), data.total_week_water(app.config["DB_FILE"], "user", datetime.now().timestamp())), 2)
    return jsonify({"savings": ("-$" if saved < 0 else "$") + str(abs(saved))})


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
