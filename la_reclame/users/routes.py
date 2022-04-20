from flask import render_template

from la_reclame.users import users


@users.route('/profile', methods=['GET'])
def profile():
    return render_template('profile.html')
