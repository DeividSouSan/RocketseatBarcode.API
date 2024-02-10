
from unittest.mock import patch
from src.controllers.create_tag_controller import CreateTagController
from src.drivers.barcode_handler import BarcodeHandler


@patch.object(BarcodeHandler, 'create_barcode')
def test_create_success(mock_barcode_handler):
    mock_product_code = "123-456-789"

    # O mock_barcode_handler será responsável por responder à chamada
    # de HandlerBarcode dentro do método create()
    mock_barcode_handler.return_value = mock_product_code

    create_tag = CreateTagController()
    tag_info = create_tag.create(mock_product_code)

    assert isinstance(tag_info, dict)
    assert "data" in tag_info
    assert "type" in tag_info["data"]
    assert "count" in tag_info["data"]
    assert "path" in tag_info["data"]
    assert tag_info["data"]["type"] == "Tag Image"
    assert tag_info["data"]["count"] == 1
    assert tag_info["data"]["path"] == f"{mock_product_code}.png"


def test_create__fail():
    mock_product_code = 123-456-789
    create_tag = CreateTagController()

    tag: dict[str, any] = None
    try:
        tag = create_tag.create(mock_product_code)
        assert False
    except Exception:
        print(tag)
        assert True
