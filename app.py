# app.py or app/__init__.py
from flask import Flask, session
from flask_session.__init__ import Session
from Login.views import board
from dashboard.views import dashboard


app = Flask(__name__)

# Load the default configuration
app.config.from_pyfile('config.py')

# register login route
app.register_blueprint(board)

# register dashboard route
app.register_blueprint(dashboard)

#session setup
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'
sess = Session()

if __name__ == '__main__':
    app.run()  # Run our application


# Load the configuration from the instance folder
# app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
# app.config.from_envvar('APP_CONFIG_FILE')

# export APP_CONFIG_FILE=/var/www/yourapp/config/production.py
# python run.py