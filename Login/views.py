from flask import Blueprint, render_template
from flask import request, Flask, redirect, url_for
from flask import render_template, redirect, url_for

board = Blueprint('board', __name__)


@board.route('/login', methods=('GET', 'POST'))  # Route for the page
def login():
	if request.method == 'GET':
		return render_template('login_page.html', num=10)
	else:
		username = request.form['username']
		password = request.form['password']
		# pass this username and password to method for sso validation
		return redirect(url_for('board.display_orkai_dashboard_page'))


@board.route('/orkai_dashboard')  # Route for the page
def display_orkai_dashboard_page():
	return render_template('orkai_dashboard.html', num=10)

