import pytest
from utils.validators import ResponseValidators


empty_payload = None

empty_dict_payload = {}

incomplete_payload = {
  "id": 398,
}

invalid_payload = {
  "id": 'string instead of int',
}

valid_payload = {
  "id": 398,
  "title": "Some title that is enough",
  "price": 0.1,
  "description": "description this description that",
  "category": "omlette",
  "image": "http://example.com"
}

@pytest.mark.parametrize(
    "method, endpoint, payload, schema_fixture, expected_status",
    [
        ("POST", "/products", valid_payload, "product_post_valid_request_schema_fixture", 201),
        ("POST", "/products", empty_payload, "product_post_bad_request_schema_fixture", 400),
        ("POST", "/products", empty_dict_payload, "product_post_bad_request_schema_fixture", 400),
        ("POST", "/products", incomplete_payload, "product_post_bad_request_schema_fixture", 400),
        ("POST", "/products", invalid_payload, "product_post_bad_request_schema_fixture", 400),
    ],
    ids=[
        "valid_payload",
        "empty_payload",
        "empty_dict_payload",
        "incomplete_payload",
        "invalid_payload"
    ]
)
def test_post(client, request, method, endpoint, payload, schema_fixture, expected_status):
    schema = request.getfixturevalue(schema_fixture)
    response = client.post(endpoint, json=payload)

    ### Soft assertions
    # Status code
    ResponseValidators.validate_status_code(response, expected_status)

    # Content type
    ResponseValidators.validate_content_type(response)

    # Schema validation for non-empty responses
    ResponseValidators.validate_schema(response, schema)
