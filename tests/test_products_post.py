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
    "method, endpoint, payload, expected_status",
    [
        ("POST", "/products", valid_payload, 201),
        ("POST", "/products", empty_payload, 400),
        ("POST", "/products", empty_dict_payload, 400),
        ("POST", "/products", incomplete_payload, 400),
        ("POST", "/products", invalid_payload, 400),
    ],
    ids=[
        "valid_payload",
        "empty_payload",
        "empty_dict_payload",
        "incomplete_payload",
        "invalid_payload"
    ]
)
def test_post(client, method, endpoint, payload, expected_status):

    response = client.post(endpoint, json=payload)
    ### Assertions
    ResponseValidators.validate_content_type(response, "application/json")
    # Response code
    assert response.status_code == expected_status
