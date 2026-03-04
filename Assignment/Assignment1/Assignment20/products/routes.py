from flask import render_template, request, redirect, make_response
from . import products_bp
import json

products = {
    "Laptop":70000,
    "Mouse":800,
    "Keyboard":1500,
    "Headphones":2000,
    "Monitor":12000
}

@products_bp.route("/")
def show_products():
    return render_template("products.html", products=products)


@products_bp.route("/add/<product>")
def add_to_cart(product):

    cart_cookie = request.cookies.get("cart")

    if cart_cookie:
        cart = json.loads(cart_cookie)
    else:
        cart = {}

    cart[product] = cart.get(product,0) + 1

    response = make_response(redirect("/cart/"))
    response.set_cookie("cart", json.dumps(cart))

    return response