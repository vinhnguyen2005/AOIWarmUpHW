
-- Tạo bảng customers
CREATE TABLE customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Thêm dữ liệu vào bảng customers
INSERT INTO customers (id, name, city) VALUES
(1, 'Alice', 'Hanoi'),
(2, 'Bob', 'Ho Chi Minh'),
(3, 'Charlie', 'Hanoi');

-- Tạo bảng orders
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Thêm dữ liệu vào bảng orders
INSERT INTO orders (id, customer_id, order_date, total) VALUES
(1, 1, '2024-01-10', 500),
(2, 1, '2024-03-01', 800),
(3, 2, '2024-02-20', 1200),
(4, 3, '2024-01-15', 200);

-- Tạo bảng products
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2)
);

-- Thêm dữ liệu vào bảng products
INSERT INTO products (id, name, price) VALUES
(1, 'Laptop', 1500),
(2, 'Mouse', 50),
(3, 'Keyboard', 100),
(4, 'Monitor', 300);

-- Tạo bảng order_items
CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Thêm dữ liệu vào bảng order_items
INSERT INTO order_items (id, order_id, product_id, quantity) VALUES
(1, 1, 2, 2),
(2, 1, 3, 1),
(3, 2, 1, 1),
(4, 2, 4, 1),
(5, 3, 1, 1);

-- Tạo bảng employees
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

-- Thêm dữ liệu vào bảng employees
INSERT INTO employees (id, name, department) VALUES
(1, 'David', 'Sales'),
(2, 'Emma', 'Support'),
(3, 'Frank', 'Sales');

-- Tạo bảng order_assignments
CREATE TABLE order_assignments (
    id INT PRIMARY KEY,
    order_id INT,
    employee_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);

-- Thêm dữ liệu vào bảng order_assignments
INSERT INTO order_assignments (id, order_id, employee_id) VALUES
(1, 1, 1),
(2, 2, 3),
(3, 3, 2);



-- Cau 1

DELIMITER //
CREATE PROCEDURE getTotalOrderCount (
    IN p_customer_id INT,
    OUT order_count INT
)
BEGIN
    SELECT COUNT(*) INTO order_count
    FROM orders
    WHERE customer_id = p_customer_id;
END //
DELIMITER ;

CALL getTotalOrderCount(1, @orderCount);
SELECT @orderCount AS total_orders;

-- Cau 2
DELIMITER //
CREATE PROCEDURE getNameEmployeeByID (
    IN employee_id INT,
    OUT employee_name varchar(255)
)
BEGIN
    SELECT name INTO employee_name
    FROM employees
    WHERE id = employee_id;
END //
DELIMITER ;

CALL getNameEmployeeByID(2, @employee_name);
SELECT @employee_name as employee_name

-- Cau 3
DELIMITER //

CREATE PROCEDURE updateCustomerCity (
    IN p_customer_id INT,
    IN p_new_city VARCHAR(100)
)
BEGIN
    UPDATE customers
    SET city = p_new_city
    WHERE id = p_customer_id;
END //

DELIMITER ;
CALL updateCustomerCity(1, 'Da Nang');
SELECT * FROM customers WHERE id = 1;

-- Cau 4
DELIMITER //

CREATE PROCEDURE productHasPriceOverX (
    IN min_price INT
)
BEGIN
   SELECT name, price
   FROM products 
   WHERE price > min_price;
END //

DELIMITER ;
CALL productHasPriceOverX(110);

-- Cau 5
DELIMITER //

CREATE PROCEDURE deleteOrderHasPriceLowerThanX (
    IN min_total INT
)
BEGIN
    DELETE FROM orders 
    WHERE total < min_total;
END //

DELIMITER ;
CALL deleteOrderHasPriceLowerThanX(700);


