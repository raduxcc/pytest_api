
# @todo: add payloads through fixtures that work with parametrize
class ProductPayloads:

    empty_payload = ''

    empty_dict_payload = {}

    incomplete_payload = {
        "id": 398,
    }

    invalid_payload = {
        "id": 'string instead of int',
    }

    valid_payload = {
        "id": 398,
        "title": "crc title test",
        "price": 0.1,
        "description": "description this description that",
        "category": "omlette",
        "image": "http://example.com"
    }

    # # needed for parametrize
    # @staticmethod
    # def all():
    #     return [
    #         ("empty", empty_payload),
    #         ("empty_dict", empty_dict_payload),
    #         ("incomplete", incomplete_payload),
    #         ("invalid", invalid_payload),
    #         ("valid", valid_payload),
    #     ]