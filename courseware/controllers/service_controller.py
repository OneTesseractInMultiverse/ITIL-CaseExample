from courseware import app
from flask import render_template

# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/service/1', methods=['GET'])
def service_1():
    return render_template("home/auth_service.html")
