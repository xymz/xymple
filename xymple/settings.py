import flask
import os.path

app = flask.Flask(__name__)

directory = os.path.dirname(__file__)
try:
    config = open(os.path.join(directory, "CONFIG"), "r")
except IOError:
    raise SystemExit("Copy `xymple/CONFIG.dist` to `xymple/CONFIG` " 
                     "and apply your own settings")
DEBUG = config.readline()
SECRET_KEY = config.readline()
URL = config.readline()

app.config.from_object(__name__)
