from flask import Blueprint, render_template

orkai_view = Blueprint('orkai_view', __name__)

@orkai_view.route('/orkai_dashboard')  # Route for the page
def display_orkai_page():
	return render_template('orkai_dashboard.html', num=10)
