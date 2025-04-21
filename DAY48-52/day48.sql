
-- Bảng customers
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Bảng orders
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Bảng products
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Bảng order_items
CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Bảng employees
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

-- Bảng order_assignments
CREATE TABLE order_assignments (
    id INT PRIMARY KEY,
    order_id INT,
    employee_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Thêm dữ liệu vào bảng customers
INSERT INTO customers VALUES
(1, 'Alice', 'Hanoi'),
(2, 'Bob', 'Ho Chi Minh'),
(3, 'Charlie', 'Hanoi');

-- Thêm dữ liệu vào bảng orders
INSERT INTO orders VALUES
(1, 1, '2024-01-10', 500),
(2, 1, '2024-03-01', 800),
(3, 2, '2024-02-20', 1200),
(4, 3, '2024-01-15', 200);

-- Thêm dữ liệu vào bảng products
INSERT INTO products VALUES
(1, 'Laptop', 1500),
(2, 'Mouse', 50),
(3, 'Keyboard', 100),
(4, 'Monitor', 300);

-- Thêm dữ liệu vào bảng order_items
INSERT INTO order_items VALUES
(1, 1, 2, 2),
(2, 1, 3, 1),
(3, 2, 1, 1),
(4, 2, 4, 1),
(5, 3, 1, 1);

-- Thêm dữ liệu vào bảng employees
INSERT INTO employees VALUES
(1, 'David', 'Sales'),
(2, 'Emma', 'Support'),
(3, 'Frank', 'Sales');

-- Thêm dữ liệu vào bảng order_assignments
INSERT INTO order_assignments VALUES
(1, 1, 1),
(2, 2, 3),
(3, 3, 2);

-- Cau 1
SELECT c.name
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.id IN (SELECT od.order_id FROM order_items od 
				JOIN products p ON od.product_id = p.id
                WHERE p.price > 1000)
                
-- Cau 2
SELECT c.name, (SELECT SUM(total) FROM orders o WHERE c.id = o.customer_id) AS total_spent
FROM customers c

-- Cau 3
SELECT name, total_spent
FROM (SELECT c.name, SUM(o.total) as total_spent FROM 
		customers c JOIN orders o ON c.id = o.customer_id
        GROUP BY c.name)
        AS Spending
ORDER BY total_spent DESC
LIMIT 2

-- Cau 4
SELECT e.name
FROM employees e
WHERE e.department = 'Sales'
AND EXISTS (SELECT 1 FROM 
			order_assignments od
            JOIN order_items ord ON od.order_id = ord.order_id
            JOIN products p ON p.id = ord.product_id
            WHERE p.name = 'Monitor' and od.employee_id = e.id)
            
-- Cau 5
SELECT c.name, SUM(o.total) AS total_spent
FROM customers c 
join orders o ON c.id = o.customer_id
GROUP BY c.name
HAVING SUM(o.total) > (SELECT AVG(total_customer) FROM
			(SELECT customer_id, SUM(total) as total_customer
            FROM orders
            GROUP BY customer_id) as average_table)
            
-- Cau 6
CREATE TEMPORARY TABLE vip_customers AS
SELECT customer_id, SUM(total) as total_spent
FROM orders 
GROUP BY customer_id
HAVING SUM(total) > 1000

SELECT c.name, v.total_spent
FROM customers c 
JOIN vip_customers v 
ON c.id = v.customer_id

-- Cau 7
CREATE TEMPORARY TABLE popular_products AS
SELECT product_id, SUM(quantity) AS total_quantity
FROM order_items
GROUP BY product_id
HAVING SUM(quantity) >= 2

SELECT p.name, po.total_quantity
FROM products p 
JOIN popular_products po
ON p.id = po.product_id

-- Cau 8
select
	c.name
from
	customers c
join orders o 
on
	c.id = o.customer_id
join order_assignments oa
on
	oa.order_id = o.id
where
	oa.employee_id in ( select 
    employee_id FROM
	(select
		e.id as employee_id,
		SUM(total) as total_sales
	from
		employees e
	join order_assignments oa 
on
		e.id = oa.employee_id
	join orders o 
on
		o.id = oa.order_id
	group by
		e.id
	having
		SUM(total) > 1000)
as sellers)

-- Cau 9
CREATE TEMPORARY TABLE high_value_orders AS 
SELECT * FROM orders 
WHERE total > 800

SELECT c.name, h.total 
FROM customers c 
JOIN high_value_orders h 
ON c.id = h.customer_id

-- Cau 10
SELECT od.order_id, SUM(od.quantity * p.price) as real_price
FROM order_items od 
JOIN products p
ON od.product_id = p.id
GROUP BY od.order_id






            

