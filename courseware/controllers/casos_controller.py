from courseware import app
from flask import render_template


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/casos', methods=['GET'])
def get_casos():
    return render_template("casos/index.html")


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/casos/business-continuity', methods=['GET'])
def get_business_continuity():
    return render_template("casos/business_continuity.html")
