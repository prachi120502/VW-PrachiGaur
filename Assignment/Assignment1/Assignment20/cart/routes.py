from flask import render_template, request, redirect, make_response
from . import cart_bp
import json

products = {
    "Laptop":70000,
    "Mouse":800,
    "Keyboard":1500,
    "Headphones":2000,
    "Monitor":12000
}


@cart_bp.route("/")
def view_cart():

    cart_cookie = request.cookies.get("cart")

    if not cart_cookie:
        return render_template("cart.html", cart={}, total=0)

    cart = json.loads(cart_cookie)

    cart_details = {}
    total = 0

    for item, qty in cart.items():

        price = products[item]
        subtotal = price * qty
        total += subtotal

        cart_details[item] = {
            "price":price,
            "qty":qty,
            "subtotal":subtotal
        }

    return render_template("cart.html", cart=cart_details, total=total)


@cart_bp.route("/update", methods=["POST"])
def update_cart():

    cart_cookie = request.cookies.get("cart")

    if not cart_cookie:
        return redirect("/cart/")

    cart = json.loads(cart_cookie)

    product = request.form.get("product")
    qty = int(request.form.get("quantity"))

    if qty == 0:
        cart.pop(product, None)
    else:
        cart[product] = qty

    response = make_response(redirect("/cart/"))
    response.set_cookie("cart", json.dumps(cart))

    return response


@cart_bp.route("/clear")
def clear_cart():

    response = make_response(redirect("/cart/"))
    response.set_cookie("cart","",expires=0)

    return response