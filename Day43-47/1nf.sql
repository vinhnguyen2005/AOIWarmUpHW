-- Câu 1:
-- Vi Phạm 1NF do ở cột stock_codes chứa nhiều giá trị trong một cột 

-- Cau 2:
CREATE TABLE stock_transactions (
    transaction_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    stock_codes VARCHAR(255),
    transaction_date DATE
);

INSERT INTO stock_transactions (transaction_id, customer_name, stock_codes, transaction_date)
VALUES 
(1, 'Nguyen Van A', 'VNM, FPT, MWG', '2024-12-01'),
(2, 'Le Thi B', 'SSI', '2024-12-02'),
(3, 'Tran Van C', 'VCB, TCB', '2024-12-03');

-- Cau 3:
CREATE TABLE stock (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_id INT,
    stock_code VARCHAR(10),
    FOREIGN KEY (transaction_id) REFERENCES stock_transactions(transaction_id)
);

INSERT INTO stock (transaction_id, stock_code) VALUES 
(1, 'VNM'),
(1, 'FPT'),
(1, 'MWG'),
(2, 'SSI'),
(3, 'VCB'),
(3, 'TCB');

-- Cau 4:
SELECT t.customer_name, s.stock_code  FROM stock_transactions t
JOIN stock s ON t.transaction_id = s.transaction_id

UPDATE stock_transactions
SET customer_name = 'Nguyen V. A'
WHERE transaction_id = 1;

DELETE FROM stock WHERE transaction_id = 1 AND stock_code = 'MWG'

-- CAU 5:
SELECT t.customer_name, COUNT(s.stock_code) AS stockcount
FROM stock_transactions t
JOIN stock s ON t.transaction_id = s.transaction_id
GROUP BY t.customer_name;

SELECT t.customer_name, COUNT(s.stock_code) AS stockcount
FROM stock_transactions t
JOIN stock s ON t.transaction_id = s.transaction_id
GROUP BY t.customer_name
ORDER BY COUNT(s.stock_code) DESC
LIMIT 1


