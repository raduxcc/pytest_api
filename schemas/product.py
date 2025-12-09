from pytest_schema import schema, And, Enum, Optional, Or, Regex, SchemaError

product_schema = schema(
    {
        "id": int,
        "title": str,
        "price": Or(int, float),
        "description": str,
        "category": str,
        "image": str,
        "rating": {
            "count": int,
            "rate": Or(int, float),
        }
    }
)

product_post_bad_request_schema = schema(
    {
        "error": str, #"Bad request"
        "message": str, #"Request body could not be read properly.",
    }
)

product_post_valid_request_schema = schema(
    {
        "id": int,
    }
)

# ### Doc example for advanced validation https://pypi.org/project/pytest-schema/
# # single user schema
# user = {
#     # id must be int
#     "id": int,
#     # name must be type str
#     "name": str,
#     # description must be type str or nullable
#     "description": Or(None, str),
#     # email valid str format
#     "email": Regex(r".*?@.*?\.[A-Za-z]{2,6}"),
#     # age converted to int then validated gt 18 lt 99 and must be type str
#     "age": And(int, lambda n: 18 <= n <= 99),
#     # gender key is optional but must be str
#     Optional("gender"): str,
#     # role of enum values
#     "role": Enum("user", "super-user", "admin"),
#     # list of ids ref friends
#     "friends": [ int ],
#     # nested dict to valid as address
#     "address": {
#         "street": str,
#         Optional("street2"): str,
#         "city": str,
#         "state": And(str, lambda s: len(s) == 2),
#         "zipcode": str,
#     }
#
# }
