from http.client import HTTPResponse
from flask import Blueprint, request, jsonify

from src.views.http_types.http_request import HttpRequest
from src.views.create_tag_view import CreateTagView
from src.errors.error_handler import handle_errors
from src.validators.create_tag_validator import create_tag_validator

tags_routes_bp = Blueprint('tags_routes', __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    response: HTTPResponse

    try:
        http_request = HttpRequest(body=request.json)
        create_tag_validator(http_request)


        create_tag_view = CreateTagView()
        response = create_tag_view.validate_and_create(http_request)

    except Exception as err:
        response = handle_errors(err)

    return jsonify(response.body), response.status_code
