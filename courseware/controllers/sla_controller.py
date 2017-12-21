from courseware import app
from flask import render_template


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/sla/1', methods=['GET'])
def sla_1():
    return render_template("servicelevel/auth_sla.html")


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/sla/2', methods=['GET'])
def sla_2():
    return render_template("servicelevel/consulting_sla.html")


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/sla/3', methods=['GET'])
def sla_3():
    return render_template("servicelevel/hosting_sla.html")