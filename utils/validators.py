
class ResponseValidators:

    def validate_status_code(response, expected_code):
        assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"

    def validate_content_type(response, expected="application/json"):
        content_type = response.headers.get("Content-Type", "")
        assert expected in content_type, f"Invalid content type: {content_type}"