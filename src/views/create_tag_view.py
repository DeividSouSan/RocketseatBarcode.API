from src.controllers.create_tag_controller import CreateTagController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class CreateTagView:
    """
    This class allows interaction with HTTP.
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        barcode = CreateTagController()
        response = barcode.create(product_code)

        return HttpResponse(response, 200)
