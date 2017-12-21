from courseware import app
from flask import render_template


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/', methods=['GET'])
def home():
    return render_template("home/index.html")


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
@app.route('/rfc', methods=['GET'])
def rfc():
    return render_template("home/request_change_form.html")