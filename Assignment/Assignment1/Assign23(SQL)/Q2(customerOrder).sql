CREATE DATABASE retail_db;
USE retail_db;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price DECIMAL(10,2)
);


CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


INSERT INTO Customers VALUES
(1,'Amit','Delhi'),
(2,'Priya','Mumbai'),
(3,'Rohit','Bangalore'),
(4,'Neha','Delhi'),
(5,'Karan','Pune');

INSERT INTO Products VALUES
(101,'Laptop',70000),
(102,'Mouse',500),
(103,'Keyboard',1500),
(104,'Monitor',12000);


INSERT INTO Orders VALUES
(1,1,'2025-01-05',70500),
(2,1,'2025-01-10',1500),
(3,1,'2025-02-01',500),
(4,1,'2025-02-10',12000),

(5,2,'2025-01-15',500),

(6,3,'2025-02-05',70000),

(7,4,'2025-03-01',12000);


INSERT INTO Order_Items VALUES
(1,1,101,1),
(2,1,102,1),

(3,2,103,1),

(4,3,102,1),

(5,4,104,1),

(6,5,102,1),

(7,6,101,1),

(8,7,104,1);


#Customers who placed more than 3 orders
SELECT c.customer_id, c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 3;

#Top 5 customers by total spending
SELECT c.customer_id, c.name, SUM(o.total_amount) AS total_spending
FROM Customers c
JOIN Orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC
LIMIT 5;

#Most ordered product
SELECT p.product_name, SUM(oi.quantity) AS total_quantity
FROM Products p
JOIN Order_Items oi
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_quantity DESC
LIMIT 1;

#Customers who never placed an order
SELECT customer_id, name
FROM Customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM Orders
);

#Total revenue generated each month
SELECT 
DATE_FORMAT(order_date,'%Y-%m') AS month,
SUM(total_amount) AS revenue
FROM Orders
GROUP BY month
ORDER BY month;