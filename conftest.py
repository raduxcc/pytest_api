import pytest
from schemas.product import product_schema
from schemas.product import product_post_bad_request_schema
from schemas.product import product_post_valid_request_schema
from config.envs import ENVIRONMENTS, DEFAULT_ENV
from utils.client import APIClient

# module-level storage for report metadata
_CURRENT_ENV = None
_CURRENT_TIMEOUT = None


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default=DEFAULT_ENV,
        help="Test environment: dev / prod",
    )


@pytest.fixture(scope="session")
def env(request):
    env_name = request.config.getoption("--env").upper()

    if env_name not in ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment '{env_name}'. "
            f"Choose from: {list(ENVIRONMENTS.keys())}"
        )

    return env_name


def pytest_configure(config):
    global _CURRENT_ENV, _CURRENT_TIMEOUT

    env = config.getoption("--env").upper()
    _CURRENT_ENV = env
    _CURRENT_TIMEOUT = ENVIRONMENTS[env]["timeout"]


# add environment details to pytest-html report
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([
        f"<p><strong>Environment:</strong> {_CURRENT_ENV}</p>",
        f"<p><strong>Timeout (seconds):</strong> {_CURRENT_TIMEOUT}</p>",
    ])


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
def client(env):
    env_config = ENVIRONMENTS[env]

    return APIClient(
        base_url=env_config["base_url"],
        timeout=env_config["timeout"],
    )


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