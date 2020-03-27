from flask import Flask
from config import Config

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)
#app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes