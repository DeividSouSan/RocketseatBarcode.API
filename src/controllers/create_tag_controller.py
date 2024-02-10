from src.drivers.barcode_handler import BarcodeHandler


class CreateTagController:
    """
    Implements business rules.
    """

    def create(self, product_code: str) -> dict[str, any]:
        path = self.__create_tag(product_code)
        response = self.__format_response(path)
        return response

    def __create_tag(self, product_code: str) -> str:
        barcode = BarcodeHandler()
        path = barcode.create_barcode(product_code)
        return path

    def __format_response(self, path: str) -> dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f"{path}.png"
            }
        }
