class HttpRequest:
    """
    This class will allow you encapsulate in a more organized way the Request header, body
    and query_params.
    """

    def __init__(
        self,
        header: dict = None,
        body: dict = None,
        query_params: dict = None
    ) -> None:

        self.header = header
        self.body = body
        self.query_params = query_params
