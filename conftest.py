import pytest
from client import APIClient
from schemas.product import product_schema
from schemas.product import product_post_bad_request_schema
from schemas.product import product_post_valid_request_schema
from payloads.products import ProductPayloads


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # attach api response if available
        response = item.funcargs.get("response", None)
        if response:
            report.extra = getattr(report, "extra", [])
            from pytest_html import extras
            report.extra.append(
                extras.text(response.text, name=f"Response: {item.name}")
            )


@pytest.fixture(scope="session")
def client():
    """Reusable API client for all tests"""
    return APIClient()


@pytest.fixture(scope="session")
def product_schema_fixture():
    return product_schema


@pytest.fixture(scope="session")
def product_post_bad_request_schema_fixture():
    return product_post_bad_request_schema


@pytest.fixture(scope="session")
def product_post_valid_request_schema_fixture():
    return product_post_valid_request_schema


# @todo: add payloads through fixtures that work with parametrize
# @pytest.fixture(params=ProductPayloads.all())
# def product_payload(request):
#     return request.param