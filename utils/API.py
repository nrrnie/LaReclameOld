from requests.exceptions import RequestException
from requests import post


class API:

    def __init__(self):
        self.host = 'http://127.0.0.1:5001'

    def register_user(self, username: str, email: str, password: str) -> str:
        url = self.host + '/auth/add/user'
        data = dict(username=username, email=email, password=password)
        try:
            response = post(url, data=data).json()
        except RequestException:
            return 'Request error'

        if response['status'] == 'ok':
            return 'ok'
        return response['error']

    def login(self, username: str, password: str) -> str:
        url = self.host + '/auth/login'
        data = dict(username=username, password=password)

        try:
            response = post(url, data=data).json()
        except RequestException:
            return 'Request error'

        if response['status'] == 'ok':
            return 'ok'

        return response['error']
