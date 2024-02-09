from barcode import Code128
from barcode.writer import ImageWriter


class BarcodeHandler:
    """
    This class is a Facade. It centralizes the Barcode creating logic so it 
    can be used for any class and update just once.
    """

    def create_barcode(self, product_code: str) -> str:
        barcode = Code128(product_code, writer=ImageWriter())
        path = f'{barcode}'
        barcode.save(path)

        return path
