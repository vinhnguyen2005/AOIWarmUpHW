create table categories (
    categoryid int primary key,
    name varchar(100)
);

insert into categories (categoryid, name) values
(1, 'áo'),
(2, 'quần'),
(3, 'váy'),
(4, 'phụ kiện');

create table products (
    productid int primary key,
    name varchar(100),
    categoryid int,
    price int,
    foreign key (categoryid) references categories(categoryid)
);

insert into products (productid, name, categoryid, price) values
(101, 'áo sơ mi nam', 1, 300000),
(102, 'quần jeans', 2, 500000),
(103, 'váy xòe', 3, 450000);

create table variants (
    variantid int primary key,
    productid int,
    color varchar(50),
    size varchar(10),
    stock int,
    foreign key (productid) references products(productid)
);

insert into variants (variantid, productid, color, size, stock) values
(1, 101, 'trắng', 'm', 20),
(2, 101, 'trắng', 'l', 15),
(3, 102, 'xanh', 'm', 10),
(4, 103, 'đỏ', 's', 5);

create table customers2 (
    customerid int primary key,
    name varchar(100),
    phone varchar(15),
    address varchar(100),
    createddate date
);

insert into customers2 (customerid, name, phone, address, createddate) values
(1, 'trần an', '0909123456', 'hà nội', '2024-01-10'),
(2, 'lê bình', '0909223456', 'tp.hcm', '2024-02-05');

create table orders (
    orderid int primary key,
    customerid int,
    orderdate date,
    status varchar(50),
    foreign key (customerid) references customers(customerid)
);

insert into orders (orderid, customerid, orderdate, status) values
(1, 1, '2024-03-01', 'đã giao'),
(2, 2, '2024-03-02', 'đã đặt');

create table orderdetails (
    orderid int,
    variantid int,
    quantity int,
    price int,
    primary key (orderid, variantid),
    foreign key (orderid) references orders(orderid),
    foreign key (variantid) references variants(variantid)
);

insert into orderdetails (orderid, variantid, quantity, price) values
(1, 1, 2, 300000),
(1, 3, 1, 500000),
(2, 4, 1, 450000);



-- cau 3
select 
    o.orderid,
    c.name as customername,
    sum(od.quantity * od.price) as totalamount
from 
    orders o
join 
    customers2 c on o.customerid = c.customerid
join 
    orderdetails od on o.orderid = od.orderid
group by 
    o.orderid, c.name;

-- cau 4
select 
    v.variantid,
    p.name as productname,
    v.color,
    v.size,
    v.stock
from 
    variants v
join 
    products p on v.productid = p.productid
where 
    v.stock < 10;

-- cau 5
select 
    day(o.orderdate) as orderday,
    sum(od.quantity * od.price) as totalrevenue
from 
    orders o
join 
    orderdetails od on o.orderid = od.orderid
group by 
    day(o.orderdate);


