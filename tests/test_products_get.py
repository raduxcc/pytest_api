import pytest
from utils.validators import ResponseValidators


@pytest.mark.parametrize(
    "method, endpoint, payload, schema_fixture, expected_status",
    [
        ("GET", "/products", None, "product_schema_fixture", 200),
        ("GET", "/products/1", None, "product_schema_fixture", 200),
        ("GET", "/products/thisisinvalid", None, "product_schema_fixture", 400),
        ("GET", "/products/99534834723", None, "product_schema_fixture", 404),
    ],
    ids=[
        "valid_get_all_products",
        "valid_get_singular_product",
        "invalid_product_id",
        "not_found_product_id",
    ]
)
def test_get(client, request, method, endpoint, payload, schema_fixture, expected_status):

    # Get schema fixture dynamically
    schema = request.getfixturevalue(schema_fixture)
    response = client.get(endpoint)

    ### Assertions
    ResponseValidators.validate_content_type(response, "application/json")
    actual_response = response.json()
    # Response code
    assert response.status_code == expected_status

    # Schema validation
    if isinstance(actual_response, list):
        for item in actual_response:
            assert item == schema
    else:
        assert actual_response == schema
