from flask import request, render_template

from la_reclame.auth import auth


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
