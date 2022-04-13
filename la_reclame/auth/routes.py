from flask import request, render_template

from la_reclame.auth import auth
from utils import api


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    username = request.form.get('username', '')
    password = request.form.get('password', '')
    email = request.form.get('email', '')

    response = api.register_user(username, email, password)
    if response == 'ok':
        return 'registered'

    return render_template('registration.html')
