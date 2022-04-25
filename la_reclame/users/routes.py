from flask import render_template

from la_reclame.users import users
from utils import api


@users.route('/<username>', methods=['GET'])
def profile(username: str):
    response = api.find_user_by_username(username)
    if response['status'] == 'ok':
        user = response['user']
        return render_template('profile.html', user=user)

    return response['error']
