create table customers(
	customerid int primary key,
	name nvarchar(255),
	city nvarchar(255)
);

create table accounts (
    accountid varchar(10) primary key,
    customerid int,
    balance int,
);


insert into customers (customerid, name, city) values
(1, 'alice', 'hanoi'),
(2, 'bob', 'hcm'),
(3, 'charlie', 'danang'),
(4, 'diana', 'hanoi');


insert into accounts (accountid, customerid, balance) values
('a1', 1, 500),
('a2', 1, 1000),
('a3', 2, 1500),
('a4', 5, 300)


-- cau 1
select
	c.name,
	a.accountid,
	a.balance
from
	customers c
join accounts a on
	c.customerid = a.customerid

-- cau 2
select name
from customers c
where exists (
    select 1
    from accounts a
    where a.customerid = c.customerid
);

-- cau 3
select
	a.accountid,
	a.customerid,
	a.balance,
	c.name,
	c.city
from
	accounts a
left join customers c on
	a.customerid = c.customerid;

-- cau 4
select
	c.customerid,
	c.name,
	a.accountid,
	a.balance
from
	customers c
cross join accounts a;

-- cau 4
select c.customerid, c.name
from customers c
where not exists (
    select 1
    from accounts a
    where a.customerid = c.customerid
);

-- Cau 5
SELECT a.AccountID, a.CustomerID, a.Balance
FROM Accounts a
WHERE NOT EXISTS (
    SELECT 1
    FROM Customers c
    WHERE c.CustomerID = a.CustomerID
);


