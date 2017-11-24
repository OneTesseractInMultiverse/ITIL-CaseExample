from courseware import app
from flask import render_template

# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/service/1', methods=['GET'])
def service_1():
    return render_template("home/auth_service.html")


# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/service/2', methods=['GET'])
def service_2():
    return render_template("home/consulting_service.html")
    

# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/service/3', methods=['GET'])
def service_3():
    return render_template("home/hosting_service.html")