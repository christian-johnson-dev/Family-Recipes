from flask import Flask
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key = "shhh"
app.config['UPLOAD_FOLDER']='./flask_app/static/uploads'

