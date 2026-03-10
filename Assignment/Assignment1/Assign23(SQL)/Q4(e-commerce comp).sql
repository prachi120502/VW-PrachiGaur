CREATE DATABASE ecommerce_db;
USE ecommerce_db;
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2)
);
INSERT INTO Orders VALUES
(1,101,201,2,4000),
(2,101,202,1,3000),
(3,101,203,3,4500),
(4,101,201,1,2000),

(5,102,202,2,6000),
(6,102,203,1,1500),

(7,103,201,4,8000),

(8,104,202,1,3000),
(9,104,201,1,2000),
(10,104,203,2,3000),
(11,104,202,3,9000),

(12,105,201,60,120000),
(13,105,201,50,100000);

#Total amount spent by each customer
SELECT customer_id,
SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;

#Number of orders placed by each customer
SELECT customer_id,
COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id;

#Customers who placed more than 3 orders
SELECT customer_id,
COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

#Customers whose total spending is greater than 10,000
SELECT customer_id,
SUM(total_amount) AS total_spending
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

#Products whose total quantity sold is greater than 100
SELECT product_id,
SUM(quantity) AS total_quantity
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;