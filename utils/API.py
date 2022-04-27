from requests.exceptions import RequestException
from requests import post


class API:

    def __init__(self):
        self.host = 'http://127.0.0.1:5001'

    def register_user(self, username: str, email: str, password: str) -> str:
        link = self.host + '/auth/add/user'
        data = dict(username=username, email=email, password=password)
        response = API.safe_request(link, data=data)
        return response if response['status'] == 'error' else response['response']

    def login(self, username: str, password: str) -> str:
        link = self.host + '/auth/login'
        data = dict(username=username, password=password)
        response = API.safe_request(link, data=data)
        return response if response['status'] == 'error' else response['response']

    def find_user_by_id(self, user_id: int) -> dict:
        link = self.host + '/users/user_by_id/{}'.format(user_id)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    def find_user_by_username(self, user_name: str) -> dict:
        link = self.host + '/users/user_by_username/{}'.format(user_name)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    def find_user_by_email(self, user_email: str) -> dict:
        link = self.host + '/users/user_by_email/{}'.format(user_email)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    # items
    def create_item(self, username:str, title: str, body: str):
        link = self.host + '/items/add/item'
        data = dict(username=username, title=title, body=body)
        try:
            response = post(link, data=data).json()
        except RequestException:
            return 'Request error'

        return response if response['status'] == 'error' else response['response']

    def find_item_by_id(self, item_id: int):
        link = self.host + '/items/item_by_id/{}'.format(item_id)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    def find_items_by_username(self, item_username: str):
        link = self.host + '/items/item_by_username/{}'.format(item_username)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    def find_items_by_title(self, item_title: str):
        link = self.host + '/items/item_by_title/{}'.format(item_title)
        response = API.safe_request(link)
        return response if response['status'] == 'error' else response['response']

    @staticmethod
    def safe_request(link: str, data: dict = None) -> dict:
        try:
            response = post(link, data=data).json()
        except RequestException:
            return dict(status='error', error='API error')

        return dict(status='ok', response=response)
