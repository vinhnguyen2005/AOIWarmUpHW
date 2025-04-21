CREATE TABLE Items (
    item_code VARCHAR(10) PRIMARY KEY,
    item_name VARCHAR(100)
);

CREATE TABLE Warehouses (
    warehouse_id VARCHAR(10) PRIMARY KEY,
    warehouse_name VARCHAR(100)
);

CREATE TABLE Customers (
    customer_id VARCHAR(10) PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE Staff (
    staff_id VARCHAR(10) PRIMARY KEY,
    staff_name VARCHAR(100)
);

CREATE TABLE StorageRecords (
    record_id VARCHAR(10) PRIMARY KEY,
    item_code VARCHAR(10),
    quantity INT,
    warehouse_id VARCHAR(10),
    location VARCHAR(50),
    customer_id VARCHAR(10),
    staff_id VARCHAR(10),
    FOREIGN KEY (item_code) REFERENCES Items(item_code),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);


-- Cau 2
-- Bang ko dat 3nf do  các thuộc tính như item_name, warehouse_name, customer_name, staff_name phu thuoc bac cầu, và ko phụ 
-- thuộc trực tiếp vào record_id mà thông qua các mã khác.

-- Cau 4
INSERT INTO Items VALUES 
('IT001', 'Motor Oil 5L'),
('IT002', 'Engine Cleaner'),
('IT003', 'Battery 12V');

INSERT INTO Warehouses VALUES 
('WH01', 'Main Warehouse'),
('WH02', 'North Depot');

INSERT INTO Customers VALUES 
('C001', 'Mekong Corp'),
('C002', 'Vina Auto'),
('C003', 'Delta Co');

INSERT INTO Staff VALUES 
('S01', 'Hoa Nguyen'),
('S02', 'Khang Tran');

INSERT INTO StorageRecords VALUES 
('R001', 'IT001', 50, 'WH01', 'Shelf A1', 'C001', 'S01'),
('R002', 'IT002', 30, 'WH01', 'Shelf B2', 'C002', 'S02'),
('R003', 'IT001', 40, 'WH02', 'Shelf C3', 'C001', 'S01'),
('R004', 'IT003', 25, 'WH01', 'Shelf A1', 'C003', 'S02');

SELECT 
    i.item_name,
    w.warehouse_name,
    SUM(sr.quantity) AS total_quantity
FROM 
    StorageRecords sr
JOIN Items i ON sr.item_code = i.item_code
JOIN Warehouses w ON sr.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name, i.item_name;

SELECT 
    c.customer_name,
    i.item_name,
    sr.quantity
FROM 
    StorageRecords sr
JOIN Customers c ON sr.customer_id = c.customer_id
JOIN Items i ON sr.item_code = i.item_code;


SELECT 
    c.customer_name
FROM 
    StorageRecords sr
JOIN Warehouses w ON sr.warehouse_id = w.warehouse_id
JOIN Customers c ON sr.customer_id = c.customer_id
WHERE w.warehouse_name = 'Main Warehouse'


SELECT S.location,w.warehouse_name FROM StorageRecords s
JOIN Warehouses w ON s.warehouse_id = w.warehouse_id

SELECT 
    w.warehouse_name,
    COUNT(DISTINCT sr.customer_id) AS total_customers
FROM 
    StorageRecords sr
JOIN Warehouses w ON sr.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name;



