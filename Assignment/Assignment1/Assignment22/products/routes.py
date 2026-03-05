from flask import Blueprint, jsonify, request, session, make_response
import json

products_bp = Blueprint("products", __name__, url_prefix="/products")


# ---------------------------
# Dummy Product Dataset
# ---------------------------

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200}
]


# ---------------------------
# API 2: Get All Products
# ---------------------------

@products_bp.route("/", methods=["GET"])
def get_products():
    return jsonify(products)


# ---------------------------
# API 3: View Product
# ---------------------------

@products_bp.route("/view/<int:product_id>", methods=["GET"])
def view_product(product_id):

    
    if "username" not in session:
        return jsonify({"error": "User not logged in"}), 401

   
    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

   
    recent = request.cookies.get("recent_products")

    if recent:
        recent_list = json.loads(recent)
    else:
        recent_list = []

  
    if product_id in recent_list:
        recent_list.remove(product_id)

    
    recent_list.insert(0, product_id)

    
    recent_list = recent_list[:5]

    response = make_response(jsonify(product))

   
    response.set_cookie("recent_products", json.dumps(recent_list))

    return response




@products_bp.route("/recent", methods=["GET"])
def get_recent_products():

    recent = request.cookies.get("recent_products")

    if not recent:
        return jsonify([])

    recent_ids = json.loads(recent)

    recent_products = []

    for pid in recent_ids:
        product = next((p for p in products if p["id"] == pid), None)
        if product:
            recent_products.append({
                "id": product["id"],
                "name": product["name"]
            })

    return jsonify(recent_products)