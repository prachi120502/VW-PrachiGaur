from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# storing products temporarily
products = []

@app.route("/")
def home():
    return "Flask Product API is running!"

# GET API - fetch all products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products)

# POST API - add new product
@app.route("/api/products", methods=["POST"])
def add_product():

    product = request.json

    products.append(product)

    return jsonify({
        "status": "success",
        "product_added": product
    })


if __name__ == "__main__":
    app.run(debug=True)