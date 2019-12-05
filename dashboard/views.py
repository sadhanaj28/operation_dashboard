from flask import session, Blueprint, request, render_template, redirect, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/orkai', methods=('GET', 'POST'))
def display_orkai_dashboard_page():
	if request.method == 'GET':
		username = session.get('username', 'not_logined')
		if username == 'not_logined':
			return redirect(url_for('board.login', error_message=''))
		return render_template('orkai_dashboard.html', num=10)

	if request.method == 'POST':
		server = request.form['server']
		source_path = request.form['source_path']
		destination_path = request.form['destination_path']
		file_name_type = request.form['file_name_type']
		file_name = request.form['file_name']

		# pass there arguments to service method
		response = ''
		success_message = 'successfully operated'
		error_message = ''
		return render_template('orkai_dashboard.html', num=10, error_message=error_message, success_message=success_message)


@dashboard.route('/purge', methods=('GET', 'POST'))
def display_purge_dashboard_page():

	if request.method == 'GET':
		username = session.get('username', 'not_logined')
		if username == 'not_logined':
			return redirect(url_for('board.login', error_message=''))
		return render_template('purge_dashboard.html')

	if request.method == 'POST':
		server = request.form['server']
		source_path = request.form['path']
		file_name_type = request.form['file_name_type']
		file_name = request.form['file_name']
		number_of_days = request.form['number_of_days']

		# pass there arguments to service method
		response = ''

		success_message = 'successfully operated'
		error_message = ''
		return render_template('purge_dashboard.html', error_message=error_message, success_message=success_message)


@dashboard.route('/cleanup', methods=('GET', 'POST'))
def display_cleanup_dashboard_page():
	if request.method == 'GET':
		username = session.get('username', 'not_logined')
		if username == 'not_logined':
			return redirect(url_for('board.login', error_message=''))
		return render_template('cleanup_dashboard.html', num=10)

	if request.method == 'POST':
		server = request.form['server']
		source_path = request.form['path']
		file_name = request.form['file_name']

		# pass there arguments to service method
		response = ''
		success_message = 'successfully operated'
		error_message = ''
		return render_template('cleanup_dashboard.html', error_message=error_message, success_message=success_message)
