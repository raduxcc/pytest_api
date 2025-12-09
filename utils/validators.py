import pytest_check as check
from schema import SchemaError


class ResponseValidators:

    @staticmethod
    def validate_status_code(response, expected_status):
        with check.check(" -- status code check"):
            check.equal(
                response.status_code,
                expected_status,
                f"Expected {expected_status}, got {response.status_code}"
            )


    @staticmethod
    def validate_content_type(response, expected="application/json; charset=utf-8"):
        with check.check(" -- content type check"):
            content_type = response.headers.get("Content-Type", "")
            check.is_in(
                expected,
                content_type,
                f"Expected '{expected}' in Content-Type header but got '{content_type}'"
            )
            return

    @staticmethod
    def validate_content_size(response):
        with check.check(" -- content size check"):
            content_size = len(response.content)
            if content_size == 0 :
                check.fail("Response size is zero. Skipping schema validation")
                return


    @staticmethod
    def validate_schema(response, expected_schema):
        with check.check(" -- schema check"):
            content_size = len(response.content)
            if content_size == 0 :
                check.fail("Response size is zero. Skipping schema validation")
                return

            response_json = response.json()

            items = response_json if isinstance(response_json, list) else [response_json]

            for index, item in enumerate(items):
                with check.check(f"Schema validation for item[{index}]"):
                    try:
                        # silent schema validation
                        expected_schema == item
                    except SchemaError as e:
                        # count failures in pytest-check with improved message
                        check.fail(
                            f"[Schema validation failed for item[{index}]]\n\n"
                            f"Actual response :::> {item}\n\n"
                            f"Expected Schema :::> {expected_schema}\n\n"
                            f"Original error  :::> {e.code.replace('\n', ' ').replace('\r', '')}\n"
                            f"------------------------------------------------------------"
                        )