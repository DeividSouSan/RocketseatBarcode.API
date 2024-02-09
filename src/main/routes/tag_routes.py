from http.client import HTTPResponse
from flask import Blueprint, request, jsonify

from src.views.http_types.http_request import HttpRequest
from src.views.create_tag_view import CreateTagView
from src.errors.error_handler import handle_errors

tags_routes_bp = Blueprint('tags_routes', __name__)


@tags_routes_bp.route("/create_tag", methods=["POST"])
def create_tags():
    response: HTTPResponse

    try:
        create_tag_view = CreateTagView()

        http_request = HttpRequest(body=request.json)

        response = create_tag_view.validate_and_create(http_request)

    except Exception as err:
        response = handle_errors(err)

    return jsonify(response.body), response.status_code
