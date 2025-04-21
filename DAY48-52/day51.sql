-- Cau 1
CREATE VIEW display_cutomers AS 
SELECT c.name, o.total
FROM orders o 
JOIN customers c 
ON c.id = o.customer_id

-- Cau 2
CREATE VIEW product_over_100 AS 
SELECT name, price 
FROM products 
WHERE price > 1000

-- Cau 3
CREATE VIEW order_over_1000 AS 
SELECT c.name, o.total
FROM orders o 
JOIN customers c 
ON c.id = o.customer_id
WHERE o.total > 1000

-- Cau 4
CREATE VIEW employees_from_sales AS 
SELECT * FROM employees
WHERE department = 'Sales';

-- Cau 5
CREATE VIEW order_items_detailed AS
SELECT oi.order_id, p.name, p.price, oi.quantity,
       (p.price * oi.quantity) AS line_total
FROM order_items oi
JOIN products p ON oi.product_id = p.id;

-- Cau 6
DROP VIEW IF EXISTS product_above_100;

-- Cau 7
CREATE VIEW full_info AS 
SELECT o.id AS order_id, c.name AS customer_name, 
       e.name AS employee_name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_assignments oa ON oa.order_id = o.id
JOIN employees e ON e.id = oa.employee_id;

-- Cau 8
CREATE VIEW product_quantity AS 
SELECT p.name, SUM(o.quantity) as total_quantity
FROM products p
JOIN order_items o
ON p.id = o.product_id
GROUP BY p.name

-- Cau 9 
CREATE VIEW view_order_from_hanoi AS 
SELECT o.* FROM orders o 
JOIN customers c 
ON o.customer_id = c.id
WHERE c.city = 'Hanoi'

-- Cau 10 
CREATE VIEW accounting_orders AS
SELECT o.id AS order_id, c.name AS customer_name, o.total
FROM orders o
JOIN customers c ON o.customer_id = c.id;
