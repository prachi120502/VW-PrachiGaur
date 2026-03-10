from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Prachi123#",
    "database": "order_system",
    "port": 3307
}


# Function to connect database
def connect_db():
    return mysql.connector.connect(**db_config)


# Function to create database and table
def setup_database():

    # connect without database first
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Prachi123#",
        port=3307
    )

    cursor = conn.cursor()

    # create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS order_system")

    cursor.close()
    conn.close()

    # connect to created database
    conn = connect_db()
    cursor = conn.cursor()

    # create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders(
            id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(120),
            quantity INT,
            price FLOAT
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()


# Home Page → Display all orders
@app.route("/")
def home():

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT *, (quantity*price) AS revenue FROM orders")

    orders = cursor.fetchall()

    # calculate total revenue
    total_revenue = sum(order["revenue"] for order in orders)

    cursor.close()
    conn.close()

    return render_template(
        "home.html",
        orders=orders,
        total_revenue=total_revenue
    )


# Add Order
@app.route("/create", methods=["GET", "POST"])
def create_order():

    if request.method == "POST":

        product = request.form["product_name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders(product_name, quantity, price) VALUES(%s,%s,%s)",
            (product, quantity, price)
        )

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for("home"))

    return render_template("create_order.html")


# Show orders with revenue > 2000
@app.route("/revenue-orders")
def revenue_orders():

    conn = connect_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *, (quantity*price) AS revenue
        FROM orders
        WHERE (quantity*price) > 2000
    """)

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("revenue_orders.html", orders=orders)


# Run application
if __name__ == "__main__":

    setup_database()

    app.run(debug=True)