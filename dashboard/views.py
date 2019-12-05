from flask import Blueprint, request, render_template, redirect

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/orkai', methods=('GET', 'POST'))
def display_orkai_dashboard_page():
	if request.method == 'GET':
		return render_template('orkai_dashboard.html', num=10)
	else:
		result = request.form
		print(result)
		server = request.form['server']
		source_path = request.form['source_path']
		destination_path = request.form['destination_path']
		file_name_type = request.form['file_name_type']
		file_name = request.form['file_name']
		success_message = 'success'
		error_message = 'failed'
		return render_template('orkai_dashboard.html', num=10, error=error_message, success=success_message)

@dashboard.route('/purge', methods=('GET', 'POST'))
def display_purge_dashboard_page():
	if request.method == 'GET':
		return render_template('purge_dashboard.html', num=10)
	else:
		return render_template('purge_dashboard.html', num=10)

@dashboard.route('/cleanup', methods=('GET', 'POST'))
def display_cleanup_dashboard_page():
	if request.method == 'GET':
		return render_template('cleanup_dashboard.html', num=10)
	else:
		return render_template('cleanup_dashboard.html', num=10)
