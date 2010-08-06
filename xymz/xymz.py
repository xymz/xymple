import flask
import db.db as db
from db.models import Pair
try:
    from settings import app
    from settings import URL
except ImportError:
    print "Copy settings.py.dist to settings.py and set it up."
    import sys
    sys.exit()

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        url = flask.request.values["url"]
        try:
            if flask.request.values["private"]:
                passcode = flask.request.values["passcode"]
        except KeyError:
            passcode = None
        pair = Pair.fromurl(url=url, passcode=passcode)
        simplified = URL % pair.uid
    except KeyError:
        url = ""
        simplified = ""
    return flask.render_template("index.html", url=url, simplified=simplified)

@app.route("/<uid>", methods=["GET", "POST"])
def xymplify(uid):
    pair = Pair.fromuid(uid)
    if pair:
        if pair.passcode:
            try:
                if pair.passcode == flask.request.values["passcode"]:
                    return flask.redirect(pair.url)
                raise ValueError("it's not valid passcode")
            except KeyError:
                flask.flash("Enter passcode", category="notification")
            except ValueError as e:
                flask.flash(e.message, category="notification")
            return flask.render_template("auth.html")
        else:
            return flask.redirect(pair.url)
    return flask.render_template("base.html")

@app.route("/favicon.ico")
def favicon():
    return ""

@app.route("/xym.html")
def home():
    return flask.render_template("home.html")

@app.route("/robot.txt")
def robot():
    return ""

@app.after_request
def shutdown_session(response):
    db.session.remove()
    return response

