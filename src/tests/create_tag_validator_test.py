
from src.errors.error_types.unprocessable_entity import HttpUnprocessableEntityError
from src.validators.create_tag_validator import create_tag_validator


class MockRequest:
    def __init__(self, body: dict[str, str]) -> None:
        self.body = body


def test_create_tag_validator_success():
    request = MockRequest(body={
        "product_code": "12345"
    })

    print(create_tag_validator(request))


def test_create_tag_validator_fail():
    request = MockRequest(body={
        "product_code": 12345
    })

    try:
        create_tag_validator(request)
        assert False
    except Exception as err:
        print(err)
        assert isinstance(err, HttpUnprocessableEntityError)
