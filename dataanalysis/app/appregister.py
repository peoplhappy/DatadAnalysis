from flask import Flask
from app.file.filehandler import file_api
from flask_cors import *
from app.errorhandler import errorhandler

webapp = Flask(__name__)
webapp.register_blueprint(file_api,url_prefix="/file")
webapp.register_blueprint(errorhandler, url_prefix='/error')
CORS(webapp, supports_credentials=True)






