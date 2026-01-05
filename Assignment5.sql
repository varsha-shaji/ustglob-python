use Employee;

select * from emp;
CREATE TABLE Orders (
    order_id INT,
    customer_id INT,
    order_date DATE,
    amount INT
);

INSERT INTO Orders VALUES (1, 101, DATE '2024-01-10', 20000);
INSERT INTO Orders VALUES (2, 101, DATE '2024-02-15', 35000);
INSERT INTO Orders VALUES (3, 102, DATE '2024-03-05', 15000);
INSERT INTO Orders VALUES (4, 103, DATE '2024-04-20', 60000);

CREATE TABLE Students (
    student_id INT,
    name VARCHAR(50)
);

CREATE TABLE Marks (
    student_id INT,
    subject VARCHAR(30),
    marks INT
);

INSERT INTO Students VALUES (1, 'Anu');
INSERT INTO Students VALUES (2, 'Rahul');

INSERT INTO Marks VALUES (1, 'Maths', 85);
INSERT INTO Marks VALUES (1, 'Science', 90);
INSERT INTO Marks VALUES (2, 'Maths', 78);
INSERT INTO Marks VALUES (2, 'Science', 82);

CREATE TABLE Sales (
    sale_id int,
    product_id int,
    sale_date DATE,
    quantity int
);

INSERT INTO Sales VALUES (1, 201, DATE '2024-01-05', 10);
INSERT INTO Sales VALUES (2, 201, DATE '2024-03-10', 15);
INSERT INTO Sales VALUES (3, 202, DATE '2023-12-20', 5);

CREATE TABLE Customers (
    customer_id int,
    customer_name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO Customers VALUES (1, 'Arun', 'Kochi');
INSERT INTO Customers VALUES (2, 'Meera', 'Kochi');
INSERT INTO Customers VALUES (3, 'John', 'Trivandrum');
INSERT INTO Customers VALUES (4, 'Anjali', 'Kozhikode');
INSERT INTO Customers VALUES (5, 'Ramesh', 'Kochi');
INSERT INTO Customers VALUES (6, 'Sana', 'Trivandrum');
INSERT INTO Customers VALUES (7, 'David', 'Kollam');
INSERT INTO Customers VALUES (8, 'Neha', 'Kochi');
INSERT INTO Customers VALUES (9, 'Vikram', 'Kozhikode');
INSERT INTO Customers VALUES (10, 'Priya', 'Thrissur');
INSERT INTO Customers VALUES (11, 'Anoop', 'Kollam');
INSERT INTO Customers VALUES (12, 'Sara', 'Trivandrum');
INSERT INTO Customers VALUES (13, 'Arjun', 'Kochi');
INSERT INTO Customers VALUES (14, 'Leena', 'Kochi');
INSERT INTO Customers VALUES (15, 'Thomas', 'Kozhikode');


CREATE TABLE Attendance (
    empno int,
    att_date DATE
);

INSERT INTO Attendance VALUES (7369, DATE '2024-01-01');
INSERT INTO Attendance VALUES (7499, DATE '2024-01-01');






-- 1.second maximum salary
SELECT ename, sal
FROM (
   SELECT ename, sal,
   RANK() OVER (ORDER BY sal DESC) AS r
   FROM emp
) ranked_emp
WHERE r = 2;



-- 2.Total Order Amount per Customer
select customer_id,sum(amount)  as total_amount
from orders
group by customer_id
having sum(amount)>50000;


-- 3.no of employees per department more than 3
SELECT deptno, COUNT(*) AS employee_count
FROM emp
GROUP BY deptno
HAVING COUNT(*) >= 3;


-- 4.Students scoring > 80 in at least two subjects
SELECT student_id
FROM Marks
WHERE marks > 80
GROUP BY student_id
HAVING COUNT(subject) >= 2;


-- 5.Employee earning more than department average
SELECT e.ename
FROM emp e
WHERE e.sal >
(
    SELECT AVG(sal)
    FROM emp
    WHERE deptno = e.deptno
);


-- 6.Total quantity sold per product in 2024
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
WHERE EXTRACT(YEAR FROM sale_date) = 2024
GROUP BY product_id;


-- 7.Top 3 Highest-Paid Employees from Each Department

SELECT empno, ename, deptno, sal,rnk
FROM (
    SELECT empno, ename, deptno, sal,
           DENSE_RANK() OVER (PARTITION BY deptno ORDER BY sal DESC) AS rnk
    FROM emp
) ranked
WHERE rnk <= 3;


-- 8.Cities with more than 5 customers
SELECT city, COUNT(*) AS customer_count
FROM Customers
GROUP BY city
HAVING COUNT(*) > 5;

-- 9.Employees with No Attendance Records
SELECT ename
FROM emp
WHERE empno NOT IN (SELECT empno FROM Attendance);

-- 10.Employee Name with Their Manager’s Name
SELECT 
    e.ename AS "Employee Name", 
    m.ename AS "Manager Name"
FROM 
    emp e
LEFT JOIN 
    emp m ON e.mgr = m.empno;

