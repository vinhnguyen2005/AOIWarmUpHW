-- Cau 1
CREATE INDEX customer_city
ON customers(city)

-- Cau 2
CREATE INDEX orders_customer
ON orders(customer_id);

-- Cau 3
CREATE UNIQUE INDEX product_name
ON products(name)

-- Cau 4
CREATE INDEX order_items_product_order
ON order_items(product_id, order_id);

-- Cau 5
EXPLAIN SELECT * FROM customers WHERE city = 'Hanoi';

-- Cau 6
DROP INDEX customer_city On customers

-- Cau 7
CREATE INDEX order_total 
ON orders(total)

-- Cau 8
CREATE INDEX employees_department
ON employees(department);

SELECT * FROM employees WHERE department = 'Sales';

-- Cau 9
EXPLAIN SELECT * FROM products WHERE price > 1000;

-- Cau 10
CREATE INDEX order_orderdate 
ON orders(order_date)




