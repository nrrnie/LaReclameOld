from flask import request, render_template, flash, session
from flask import redirect, url_for

from la_reclame.items import items
from utils import api

@items.route('/add/item', methods=['GET', 'POST'])
def create_item():
	if session.get('user') is None:
		return redirect(url_for('auth.login'))
	if request.method == 'GET':
		return render_template('add_item.html')

	item_username = session['user']['username']
	item_title = request.form.get('title')
	item_body = request.form.get('body')

	if None in [item_title, item_body]:
		return 'Not all data was given.'

	response = api.create_item(username=item_username, title=item_title, body=item_body)

	if response == 'ok':
		return 'item added'
	return render_template('add_item.html')
