from flask import Blueprint, jsonify, request

from app.services import generate_report, log_api_request

api = Blueprint("api", __name__)


@api.route("/log", methods=["POST"])
def log():
    return log_api_request(request.json)


@api.route("/report", methods=["GET"])
def report():
    return generate_report(request.args)


def register_routes(app):
    app.register_blueprint(api)
