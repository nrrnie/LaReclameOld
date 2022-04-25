from flask import request, render_template, flash, get_flashed_messages

from la_reclame.auth import auth
from utils import api


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')

    username = request.form.get('username', '')
    password = request.form.get('password', '')
    password_confirm = request.form.get('confirm-password', '')
    email = request.form.get('email', '')

    if None in [username, email, password]:
        flash('Not all data was given')
    if not email.find('@astanait.edu.kz'):
        flash('University e-mail address is required.')
    check_passwords(password, password_confirm)

    response = api.find_user_by_username(username)
    if response['status'] == 'ok':
        flash('Username is already taken')
    elif response['error'] == 'API error':
        flash('Can\'t connect to API')

    response = api.find_user_by_email(email)
    if response['status'] == 'ok':
        flash('Username is already taken')
    elif response['error'] == 'API error':
        flash('Can\'t connect to API')

    if len(get_flashed_messages()) != 0:
        return render_template('registration.html')

    register_user(username, email, password)
    return 'main page'


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username', '')
    password = request.form.get('password', '')

    response = api.login(username, password)
    if response['status'] == 'ok':
        return 'main page'

    flash(response['error'])
    return render_template('login.html')


def check_passwords(password: str, password_confirm: str) -> bool:
    is_ok = True
    if len(password) < 8:
        is_ok = False
        flash('Password length should be more than 7 characters')

    if password != password_confirm:
        is_ok = False
        flash('Passwords does not match')

    return is_ok


# if function returns true: users is registered
# Otherwise, users is not registered
def register_user(username, email, password):
    api.register_user(username, email, password)