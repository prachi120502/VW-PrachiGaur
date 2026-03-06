CREATE DATABASE company_db;
USE company_db;
CREATE TABLE Employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
department VARCHAR(50),
salary INT,
joining_date DATE
);

CREATE TABLE Projects (
project_id INT PRIMARY KEY,
project_name VARCHAR(50),
start_date DATE,
end_date DATE
);

CREATE TABLE Employee_Project (
emp_id INT,
project_id INT,
hours_worked INT,
rating DECIMAL(2,1),
FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

INSERT INTO Employees VALUES
(1,'Rahul','IT',70000,'2021-01-10'),
(2,'Priya','HR',60000,'2020-03-15'),
(3,'Amit','IT',80000,'2019-07-01'),
(4,'Neha','Finance',75000,'2022-02-20'),
(5,'Rohan','IT',65000,'2023-05-12');


INSERT INTO Projects VALUES
(101,'AI System','2024-01-01','2024-06-01'),
(102,'Web Portal','2024-02-01','2024-07-01'),
(103,'Mobile App','2024-03-01','2024-08-01'),
(104,'Data Migration','2024-01-15','2024-05-30');


INSERT INTO Employee_Project VALUES
(1,101,120,4.5),
(1,102,100,4.2),
(1,103,90,4.8),
(2,101,60,3.8),
(2,104,70,4.1),
(3,101,110,4.7),
(3,102,120,4.9),
(4,104,80,4.0);


SELECT * FROM Employees;


#Employees who worked on more than 2 projects

SELECT e.emp_id, e.emp_name, COUNT(ep.project_id) AS total_projects
FROM Employees e
JOIN Employee_Project ep
ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 2;

#Employees with average rating above 4

SELECT e.emp_id, e.emp_name, AVG(ep.rating) AS avg_rating
FROM Employees e
JOIN Employee_Project ep
ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING AVG(ep.rating) > 4;

#Highest paid employee in each department
SELECT department, emp_name, salary
FROM Employees e
WHERE salary = (
SELECT MAX(salary)
FROM Employees
WHERE department = e.department
);

#Employees who never worked on any project

SELECT emp_id, emp_name
FROM Employees
WHERE emp_id NOT IN (
SELECT emp_id FROM Employee_Project
);

#Project with highest hours
SELECT p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep
ON p.project_id = ep.project_id
GROUP BY p.project_name
ORDER BY total_hours DESC
LIMIT 1;