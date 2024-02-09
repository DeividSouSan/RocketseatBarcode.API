from cerberus import Validator
from src.errors.error_types.unprocessable_entity import HttpUnprocessableEntityError

from src.views.http_types.http_request import HttpRequest


def create_tag_validator(request: HttpRequest) -> None:
    body_validator = Validator({
        "product_code": {
            "type": "string",
            "required": True,
            "empty": False
        }
    })

    result = body_validator.validate(request.body)

    if result is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
