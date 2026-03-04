from flask import render_template
from . import orders_bp

@orders_bp.route("/success")
def success():
    return render_template("order_success.html")