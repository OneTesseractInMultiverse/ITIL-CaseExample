import datetime
# Turns on debugging features in Flask
DEBUG = True
#
# For use in web_app emails
MAIL_FROM_EMAIL = "info@cicc-cr.org"
#
# This is a secret key that is used by Flask to sign cookies.
# Its also used by extensions like Flask-Bcrypt. You should
# define this in your instance folder to keep it out of version
# control.
SECRET_KEY = 'f4WA8K34TrKdzzTPt'  # Change for production
#
# Configuration for the Flask-Bcrypt extension
BCRYPT_LEVEL = 12
#
# ----------------------------------------------------------------
# SLACK CONFIG
# ----------------------------------------------------------------
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"
# ----------------------------------------------------------------
# GOOGLE API CONFIGURATIONS
# ----------------------------------------------------------------
GGL_API_KEY = "AIzaSyB87KQUQJKXblfjoEP5GhPMGpT1fU8Dd4c"
# ----------------------------------------------------------------
# JWT CONFIGURATIONS
# ----------------------------------------------------------------
JWT_AUTH_URL_RULE = '/api/v1/auth'
JWT_EXPIRATION_DELTA = datetime.timedelta(3200)  # Set the token validity

# ----------------------------------------------------------------
# MONGO DATABASE CONFIGURATION
# ----------------------------------------------------------------
# MongoDB configuration parameters
MONGODB_DB = 'cafh-courseware'
MONGODB_HOST = 'ds052649.mlab.com'
MONGODB_PORT = 52649
MONGODB_USERNAME = 'xa'
MONGODB_PASSWORD = 'Wstinol123.'

# ----------------------------------------------------------------
# ELASTICSEARCH
# ----------------------------------------------------------------
ELASTICSEARCH_HOST = 'http://elasticsearch.subvertic.com:9200'