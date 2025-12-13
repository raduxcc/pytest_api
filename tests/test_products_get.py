import pytest
from utils.validators import ResponseValidators


@pytest.mark.parametrize(
    "method, endpoint, schema_fixture, expected_status, max_reponse_ms",
    [
        ("GET", "/products", "product_schema_fixture", 200, 250),
        ("GET", "/products/1", "product_schema_fixture", 200, 200),
        ("GET", "/products/thisisinvalid", "product_schema_fixture", 400, 200),
        ("GET", "/products/995348347233", "product_schema_fixture", 404, 200),
    ],
    ids=[
        "valid_get_all_products",
        "valid_get_singular_product",
        "invalid_product_id",
        "not_found_product_id",
    ]
)
def test_get(client, request, method, endpoint, schema_fixture, expected_status, max_reponse_ms):

    # Get schema fixture dynamically
    schema = request.getfixturevalue(schema_fixture)
    response = client.get(endpoint)

    ### Soft assertions
    # Status code
    ResponseValidators.validate_status_code(response, expected_status)

    # Content type
    ResponseValidators.validate_content_type(response)

    # Response time validation
    ResponseValidators.validate_response_time(response, max_reponse_ms)

    # Schema validation for non-empty responses
    ResponseValidators.validate_schema(response, schema)
