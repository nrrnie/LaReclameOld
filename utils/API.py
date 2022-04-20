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

    def find_user_by_id(self, user_id: int) -> dict:
        link = self.host + '/users/user_by_id/{}'.format(user_id)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response

    def find_user_by_username(self, user_name: str) -> dict:
        link = self.host + '/users/user_by_username/{}'.format(user_name)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response

    def find_user_by_email(self, user_email: str) -> dict:
        link = self.host + '/users/user_by_email/{}'.format(user_email)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response

    @staticmethod
    def safe_request(link: str, data: dict = None) -> dict:
        try:
            response = post(link, data=data).json()
        except RequestException:
            return {'status': 'error', 'response': response}
