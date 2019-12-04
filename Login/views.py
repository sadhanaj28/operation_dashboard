from flask import Blueprint, render_template

login_view = Blueprint('login_view', __name__)

@login_view.route('/')  # Route for the page
def display_login_page():
	return render_template('login_page.html', num=10)