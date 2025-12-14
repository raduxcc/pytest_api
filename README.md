# Pytest-based lightweight API testing framework

Libraries used:
- __pytest-check__ for soft assertions
- __pytest-schema__ to validate response structure and types
- __pytest-html__ to generate HTML test reports for pytest runs

Current tests are covering some of the API endpoints generously offered by https://fakestoreapi.com/docs#tag/Products
- GET all products
- GET a single product
- Add a new product (POST)

## Project Structure:

```
pytestAPI/
├── schemas/                   # Response schemas for validation
│   └── product.py             
├── test_reports/              
│   └── report.html            # Auto-generated HTML test report
├── tests/                     
│   ├── test_products_get.py   # Test file for GET product endpoints
│   └── test_products_post.py  # Test file for POST product endpoints
├── utils/                     
│   ├── validators.py          # Assertion methods (status, content-type, schema)
│   └── client.py              # API client wrapper (GET/POST requests)
├── pytest.ini                 # Pytest configuration file
└── conftest.py                # Pytest fixtures (client, schema fixtures)
```

## Assertions

1) Hard assertion:
- Response content type - due to framework currently handling only json responses

2) Soft assertions:
- Status code - to confirm that the API request returned the correct HTTP status code
- Schema validation for non-empty responses - to validate that the response structure and data types match the expected schema

Failures are collected and displayed in the pytest-html report without stopping test execution.

## Running tests:
1) install dependencies:
>pip install -r requirements.txt
2) to run all tests:
>pytest

After test runs, test reports are generated in either:
- *<root_folder>/test_reports* if tests are running from CLI
- *<root_folder>/tests/test_reports* when tests are being ran from IDE


### Test run GIF

![Test run demo](./demo/test_run.gif)
