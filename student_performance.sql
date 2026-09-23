CREATE DATABASE IF NOT EXISTS student_performance;
USE student_performance;

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    department VARCHAR(30),
    semester INT,
    marks DECIMAL(5,2),
    attendance DECIMAL(5,2)
);

INSERT INTO students (name, department, semester, marks, attendance)
VALUES
('Aarav', 'CSE', 2, 85.5, 92),
('Priya', 'CSE', 2, 78, 88),
('Rahul', 'ENTC', 2, 91, 95),
('Ananya', 'CSE', 2, 67.5, 81),
('Rohan', 'IT', 2, 74, 86);

SELECT * FROM students;

SELECT name, department, marks, attendance,
CASE
    WHEN marks >= 85 AND attendance >= 90 THEN 'Excellent'
    WHEN marks >= 70 AND attendance >= 75 THEN 'Good'
    WHEN marks >= 50 THEN 'Average'
    ELSE 'Needs Improvement'
END AS performance
FROM students
ORDER BY marks DESC;

SELECT name, marks
FROM students
WHERE marks > 80;

SELECT department, AVG(marks) AS average_marks
FROM students
GROUP BY department;

SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1;

SELECT AVG(marks) AS average_marks,
       MAX(marks) AS highest_marks,
       MIN(marks) AS lowest_marks
FROM students;

SELECT department, COUNT(*) AS total_students
FROM students
GROUP BY department;
        