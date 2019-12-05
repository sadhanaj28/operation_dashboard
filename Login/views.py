from flask import Blueprint, render_template
from flask import request, session
from flask import render_template, redirect, url_for
from flask_session.__init__ import Session


# from dashboard.views import dashboard

board = Blueprint('board', __name__)


@board.route('/login', methods=('GET', 'POST'))  # Route for the page
def login():
	success_message = ''
	error_message = ''
	if request.method == 'GET':
		if 'error_message' in request.args:
			error_message = request.args.get('error_message')
		return render_template('login_page.html', num=10, error_message=error_message)

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		# pass this username and password to method for sso validation
		response = 1
		if response == 1:
			session['username'] = username
			success_message = 'successfully operated'
		else:
			error_message = 'invalid user credential'

		if success_message:
			return redirect(url_for('dashboard.display_orkai_dashboard_page'))
		else:
			return redirect(url_for('board.login', error_message=error_message))


@board.route('/logout')  # Route for the page
def logout():
	session.clear()
	return redirect(url_for('board.login'))
