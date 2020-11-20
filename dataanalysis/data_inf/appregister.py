from flask import Flask
from dataanalysis.data_inf.filehandler import file_api
from flask_cors import *
import os
app = Flask(__name__,template_folder="../templates")
app.register_blueprint(file_api,url_prefix="/file")
CORS(app, supports_credentials=True)




if __name__ == "__main__":
    print(app.url_map)
    app.run()