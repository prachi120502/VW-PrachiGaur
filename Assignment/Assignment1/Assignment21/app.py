from flask import Flask, request, jsonify
import csv
import io

app = Flask(__name__)

# In-memory product storage
products = []

# -------------------------------
# Helper Function: Validate Row
# -------------------------------

def validate_product(name, price, stock):
    try:
        # Name validation
        if not name or name.strip() == "":
            return False

        # Price validation
        price = float(price)
        if price <= 0:
            return False

        # Stock validation
        stock = int(stock)
        if stock < 0:
            return False

        return True

    except:
        return False


# -------------------------------
# API: Upload CSV File
# -------------------------------

@app.route('/upload-products', methods=['POST'])
def upload_products():

    if 'file' not in request.files:
        return jsonify({"error": "CSV file not provided"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Read file content
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    csv_reader = csv.DictReader(stream)

    total_rows = 0
    products_added = 0
    failed_rows = 0

    for row in csv_reader:

        total_rows += 1

        name = row.get("name")
        price = row.get("price")
        stock = row.get("stock")

        if validate_product(name, price, stock):

            product = {
                "name": name.strip(),
                "price": float(price),
                "stock": int(stock)
            }

            products.append(product)
            products_added += 1

        else:
            failed_rows += 1

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    })


# -------------------------------
# API: Get Stored Products
# -------------------------------

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# -------------------------------
# Run Server
# -------------------------------

if __name__ == '__main__':
    app.run(debug=True)