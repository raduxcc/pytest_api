import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, endpoint: str):
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
        )

    def post(self, endpoint: str, json=None):
        return self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=json,
            timeout=self.timeout,
        )

    def put(self, endpoint: str, json=None):
        return self.session.put(
            url=f"{self.base_url}{endpoint}",
            json=json,
            timeout=self.timeout,
        )

    def delete(self, endpoint: str):
        return self.session.delete(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
        )
