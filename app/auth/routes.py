from flask import Blueprint, request, jsonify, current_app
from app.auth.schemas import LoginRequest
from app.auth.services import authenticate_user

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    login_req = LoginRequest.from_dict(data)

    token = authenticate_user(
        username=login_req.username,
        password=login_req.password,
        config=current_app.config
    )

    return jsonify({"access_token": token, "token_type": "Bearer"}), 200
