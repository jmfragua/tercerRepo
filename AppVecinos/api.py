import os
from flask import Blueprint, current_app, jsonify, request

api_bp = Blueprint("api", __name__, url_prefix="/api")

NEIGHBORS = [
    {"id": 1, "name": "Alice García", "apartment": "1A"},
    {"id": 2, "name": "Bob Martínez", "apartment": "1B"},
    {"id": 3, "name": "Carlos López", "apartment": "2A"},
]


def _is_authenticated(req):
    valid_token = current_app.config.get("API_TOKEN", os.environ.get("API_TOKEN", ""))
    auth_header = req.headers.get("Authorization", "")
    return bool(valid_token) and auth_header == f"Bearer {valid_token}"


@api_bp.route("/neighbors", methods=["GET"])
def get_neighbors():
    if not _is_authenticated(request):
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(NEIGHBORS), 200
