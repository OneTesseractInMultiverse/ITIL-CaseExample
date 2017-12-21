from courseware import app
from flask import render_template

# --------------------------------------------------------------------------
# GET /
# --------------------------------------------------------------------------
# Root resource
@app.route('/cm/index', methods=['GET'])
def change_management_home():
    return render_template("cm/index.html")