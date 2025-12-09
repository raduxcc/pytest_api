Pytest-based lightweight API testing framework

Libraries used:
- __pytest-check__ for soft assertions
- __pytest-schema__ to validate response structure and types
- __pytest-html__ to generate HTML test reports for pytest runs

Current tests are covering some of the API endpoints generously offered by https://fakestoreapi.com/docs#tag/Products
- GET all products
- GET a single product
- Add a new product (POST)

Test cases:

| Test Case ID | Title                                  | Method | Endpoint                | Input / Payload                   | Schema Fixture                            | Expected Status | Steps                                                                                                                                      | Notes                               |
| ------------ | -------------------------------------- | ------ | ----------------------- | --------------------------------- | ----------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| TC01         | Get all products                       | GET    | /products               | —                                 | product_schema_fixture                    | 200             | 1. Send GET request to `/products`<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema           | Retrieve all products               |
| TC02         | Get a single product                   | GET    | /products/1             | —                                 | product_schema_fixture                    | 200             | 1. Send GET request to `/products/1`<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema         | Retrieve a specific valid product   |
| TC03         | Invalid product ID                     | GET    | /products/thisisinvalid | —                                 | product_schema_fixture                    | 400             | 1. Send GET request with invalid ID<br>2. Validate status code<br>3. Validate Content-Type                                                 | Test with an invalid ID format      |
| TC04         | Product not found                      | GET    | /products/995348347233  | —                                 | product_schema_fixture                    | 404             | 1. Send GET request with non-existent ID<br>2. Validate status code<br>3. Validate Content-Type                                            | Test with a non-existing product ID |
| TC05         | Create product with valid payload      | POST   | /products               | valid_payload                     | product_post_valid_request_schema_fixture | 201             | 1. Send POST request with valid payload<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema      | Valid product creation              |
| TC06         | Create product with empty payload      | POST   | /products               | `None`                            | product_post_bad_request_schema_fixture   | 400             | 1. Send POST request with empty body<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema         | Empty request body                  |
| TC07         | Create product with empty object       | POST   | /products               | `{}`                              | product_post_bad_request_schema_fixture   | 400             | 1. Send POST request with empty JSON object<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema  | Empty JSON object                   |
| TC08         | Create product with incomplete payload | POST   | /products               | `{"id": 398}`                     | product_post_bad_request_schema_fixture   | 400             | 1. Send POST request with incomplete payload<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema | Missing required fields             |
| TC09         | Create product with invalid payload    | POST   | /products               | `{"id": "string instead of int"}` | product_post_bad_request_schema_fixture   | 400             | 1. Send POST request with invalid payload<br>2. Validate status code<br>3. Validate Content-Type<br>4. Validate response against schema    | Field type mismatch                 |


Assertions:

1) Hard assertion:
- Response content type - due to framework currently handling only json responses

2) Soft assertions:
- Status code - to confirm that the API request returned the correct HTTP status code
- Schema validation for non-empty responses - to validate that the response structure and data types match the expected schema

Failures are collected and displayed in the pytest-html report without stopping test execution.

Running tests:
1) install dependencies:
>pip install -r requirements.txt
2) to run all tests:
>pytest

After test runs, test reports are generated in either:
- *<root_folder>/test_reports* if tests are running from CLI
- *<root_folder>/tests/test_reports* when tests are being ran from IDE


Test run GIF:

[![api-tests-run-light.gif](https://i.postimg.cc/9Qb9BCqM/api-tests-run-light.gif)](https://postimg.cc/sMB1jFmd)


Test report screenshots:

CLI[![api-cli-run.png](https://i.postimg.cc/RF0nYK9H/api-cli-run.png)](https://postimg.cc/gwfJXwxz)

HTML[![api-html-report-example.png](https://i.postimg.cc/3R6Z7Y8Q/api-html-report-example.png)](https://postimg.cc/ygmRyq3L)