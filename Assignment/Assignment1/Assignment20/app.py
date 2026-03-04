from flask import Flask, redirect
from products.routes import products_bp
from cart.routes import cart_bp
from orders.routes import orders_bp

app = Flask(__name__)

app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)


@app.route("/")
def home():
    return redirect("/products/")


if __name__ == "__main__":
    app.run(debug=True)