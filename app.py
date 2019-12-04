# app.py or app/__init__.py
from flask import Flask
from Login.views import board

app = Flask(__name__)
# Load the default configuration
app.config.from_pyfile('config.py')

# register login route
app.register_blueprint(board)

# @app.route("/")
# def login():
#     return redirect('/dashboard.html')

if __name__ == '__main__':
    app.run()  # Run our application


# def create_app(config_file):
# 	app.config.from_pyfile(config_file)  # Configure application with settings file, not strictly necessary
# 	app.register_blueprint(login_view)  # Register url's so application knows what to do
# 	return app

# Load the configuration from the instance folder
# app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar('APP_CONFIG_FILE')

# export APP_CONFIG_FILE=/var/www/yourapp/config/production.py
# python run.py