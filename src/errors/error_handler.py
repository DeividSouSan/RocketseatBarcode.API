from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    return HttpResponse(
        {
            "error": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        },
        500
    )
