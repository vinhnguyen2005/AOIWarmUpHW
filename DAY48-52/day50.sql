
-- Cau 1
DELIMITER //

CREATE TRIGGER log_order_delete
AFTER DELETE ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_logs(log_message)
    VALUES (CONCAT('Deleted order ID: ', OLD.id));
END;

DELIMITER ;

-- Cau 2
DELIMITER //

CREATE TRIGGER update_order_total
AFTER INSERT ON order_items
FOR EACH ROW 
BEGIN
    UPDATE orders
    SET total = total + (
        SELECT price FROM products WHERE id = NEW.product_id
    ) * NEW.quantity
    WHERE id = NEW.order_id;
END;
//

DELIMITER ;

-- Trước khi thêm mới
SELECT * FROM orders WHERE id = 4;

-- Thêm sản phẩm mới vào đơn hàng id = 4
INSERT INTO order_items (order_id, product_id, quantity) 
VALUES (4, 2, 3); 

-- Kiểm tra lại total
SELECT * FROM orders WHERE id = 4;

SHOW TRIGGERS;

-- Cau 3
DELIMITER //

CREATE TRIGGER prevent_from_update_price
BEFORE UPDATE ON products
FOR EACH ROW 
BEGIN
    IF NEW.price > 1000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Can not update price!';
    END IF;
END;
//

DELIMITER ;


UPDATE products
SET price = 1600
WHERE id = 1;

-- Cau 4
CREATE TABLE customers_deleted (
    id INT,
    name VARCHAR(100),
    city VARCHAR(100),
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER insert_deleted_customer_table
BEFORE DELETE ON customers
FOR EACH ROW 
BEGIN
    INSERT INTO customers_deleted(id, name, city)
    VALUES (OLD.id, OLD.name, OLD.city);
END;
//

DELIMITER ;

-- Cau 5
CREATE TABLE order_alerts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    alert_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER insert_order_alerts
AFTER INSERT ON orders
FOR EACH ROW 
BEGIN
    IF NEW.total > 1000 AND 
       (SELECT city FROM customers WHERE id = NEW.customer_id) = 'Hanoi' THEN
        INSERT INTO order_alerts(alert_message) 
        VALUES (CONCAT('Cannot make order! (Customer from Ha Noi with id: ', NEW.customer_id, ')'));
    END IF;
END;
//

DELIMITER ;


