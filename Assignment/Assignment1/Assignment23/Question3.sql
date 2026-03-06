CREATE DATABASE employee_analysis;
USE employee_analysis;
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);
INSERT INTO Employees VALUES
(1,'Rahul','IT',70000),
(2,'Priya','HR',60000),
(3,'Amit','IT',90000),
(4,'Neha','Finance',75000),
(5,'Rohan','IT',65000),
(6,'Karan','HR',80000),
(7,'Sneha','Finance',72000),
(8,'Vikas','IT',95000);

#Employees whose salary is greater than the average salary of all employees
SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);

#Employees whose salary is greater than the average salary of their department
SELECT e.emp_id, e.emp_name, e.department, e.salary
FROM Employees e
WHERE e.salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department
);

#Employees who earn the highest salary in their department
SELECT emp_id, emp_name, department, salary
FROM Employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

#Employees who earn less than the highest salary in the company but more than the average salary
SELECT emp_id, emp_name, salary
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees)
AND salary < (SELECT MAX(salary) FROM Employees);

#Departments whose average salary is greater than the company’s average salary

SELECT department, AVG(salary) AS avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM Employees
);