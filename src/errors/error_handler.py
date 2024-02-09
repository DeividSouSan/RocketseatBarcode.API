from src.errors.error_types.unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(
            {
                "error": [{
                    "title": error.name,
                    "detail": error.message
                }]
            },
            error.status_code
        )

    return HttpResponse(
        {
            "error": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        },
        500
    )
