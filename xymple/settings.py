import flask
import os.path

app = flask.Flask(__name__)

directory = os.path.dirname(__file__)
config = open(os.path.join(directory, "CONFIG"), "r")
DEBUG = config.readline()
SECRET_KEY = config.readline()
URL = config.readline()

app.config.from_object(__name__)
