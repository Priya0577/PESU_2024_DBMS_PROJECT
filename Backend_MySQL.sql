DROP DATABASE WORKFROMHOME;
CREATE DATABASE IF NOT EXISTS WorkFromHome;
USE WorkFromHome;

CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Email VARCHAR(100),
        Position VARCHAR(50)
    );
    
CREATE TABLE IF NOT EXISTS Locations(
		EmployeeID INTEGER,
		City TEXT,
		Country TEXT,
		Continent TEXT,
		LocalTime1 TIME,
		FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
	);
    
CREATE TABLE IF NOT EXISTS Project (
		ProjectID INTEGER PRIMARY KEY,
		ProjectName TEXT NOT NULL,
		Details TEXT,
		StartDate DATE,
		EndDate DATE,
		EmployeeID INTEGER,
        FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
	);
    
CREATE TABLE IF NOT EXISTS Meeting (
		MeetingID INTEGER PRIMARY KEY,
		MeetingDate DATE,
		MeetingTime TIME,
		EmployeeID INTEGER,
		ProjectID INTEGER,
		FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
		FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
	);
    
DELIMITER //
CREATE PROCEDURE GetManagerCount
BEGIN
	SELECT * FROM EMPLOYEE WHERE POSITION='Manager';
END;
DELIMITER ;


INSERT INTO Employee (EmployeeID, FirstName, LastName, Email, Position) 
VALUES 
('1', 'Aarav', 'Sharma', 'aarav.sharma@email.com', 'Software Engineer'),
('2', 'Isha', 'Gupta', 'isha.gupta@email.com', 'Project Manager'),
('3', 'Ravi', 'Patel', 'ravi.patel@email.com', 'HR Manager'),
('4', 'Priya', 'Singh', 'priya.singh@email.com', 'Data Scientist'),
('5', 'Rahul', 'Verma', 'rahul.verma@email.com', 'Data Analyst'),
('6', 'Simran', 'Kaur', 'simran.kaur@email.com', 'Marketing Specialist'),
('7', 'Kunal', 'Desai', 'kunal.desai@email.com', 'Product Manager'),
('8', 'Meera', 'Iyer', 'meera.iyer@email.com', 'Software Engineer'),
('9', 'Amit', 'Mehta', 'amit.mehta@email.com', 'Database Administrator'),
('10', 'Ritu', 'Garg', 'ritu.garg@email.com', 'UI/UX Designer'),
('11', 'Vikram', 'Rao', 'vikram.rao@email.com', 'Network Engineer'),
('12', 'Nidhi', 'Sharma', 'nidhi.sharma@email.com', 'QA Engineer'),
('13', 'Ankit', 'Mishra', 'ankit.mishra@email.com', 'Software Developer'),
('14', 'Sneha', 'Bhatia', 'sneha.bhatia@email.com', 'HR Specialist'),
('15', 'Raj', 'Kumar', 'raj.kumar@email.com', 'Project Lead'),
('16', 'Leena', 'Kapoor', 'leena.kapoor@email.com', 'Content Writer'),
('17', 'Deepak', 'Singh', 'deepak.singh@email.com', 'Systems Analyst'),
('18', 'Swati', 'Joshi', 'swati.joshi@email.com', 'Operations Manager'),
('19', 'Rohan', 'Malhotra', 'rohan.malhotra@email.com', 'Software Architect'),
('20', 'Kavya', 'Menon', 'kavya.menon@email.com', 'Frontend Developer'),
('21', 'Suresh', 'Nair', 'suresh.nair@email.com', 'Backend Developer'),
('22', 'Pooja', 'Arora', 'pooja.arora@email.com', 'Business Analyst'),
('23', 'Mohit', 'Roy', 'mohit.roy@email.com', 'System Administrator'),
('24', 'Neha', 'Pandey', 'neha.pandey@email.com', 'Cloud Engineer'),
('25', 'Aditya', 'Rathore', 'aditya.rathore@email.com', 'Security Analyst');

INSERT INTO Locations (EmployeeID, City, Country, Continent, LocalTime1) 
VALUES 
(1, 'Mumbai', 'India', 'Asia', '10:30:00'),
(2, 'Delhi', 'India', 'Asia', '14:00:00'),
(3, 'Bangalore', 'India', 'Asia', '08:15:00'),
(4, 'Chennai', 'India', 'Asia', '09:45:00'),
(5, 'Kolkata', 'India', 'Asia', '11:00:00'),
(6, 'Hyderabad', 'India', 'Asia', '13:00:00'),
(7, 'Pune', 'India', 'Asia', '09:00:00'),
(8, 'Ahmedabad', 'India', 'Asia', '10:15:00'),
(9, 'Surat', 'India', 'Asia', '07:45:00'),
(10, 'Jaipur', 'India', 'Asia', '12:30:00'),
(11, 'Patna', 'India', 'Asia', '11:45:00'),
(12, 'Ludhiana', 'India', 'Asia', '10:50:00'),
(13, 'Bhopal', 'India', 'Asia', '08:30:00'),
(14, 'Agra', 'India', 'Asia', '13:15:00'),
(15, 'Varanasi', 'India', 'Asia', '14:45:00'),
(16, 'Nagpur', 'India', 'Asia', '12:10:00'),
(17, 'Kanpur', 'India', 'Asia', '09:25:00'),
(18, 'Lucknow', 'India', 'Asia', '07:55:00'),
(19, 'Coimbatore', 'India', 'Asia', '08:40:00'),
(20, 'Indore', 'India', 'Asia', '10:20:00'),
(21, 'Thane', 'India', 'Asia', '09:35:00'),
(22, 'Ghaziabad', 'India', 'Asia', '10:05:00'),
(23, 'Faridabad', 'India', 'Asia', '08:50:00'),
(24, 'Rajkot', 'India', 'Asia', '11:20:00'),
(25, 'Meerut', 'India', 'Asia', '13:30:00');

INSERT INTO Project (ProjectID, ProjectName, Details, StartDate, EndDate) 
VALUES 
('1', 'AI Development', 'Developing AI-based software for healthcare.', '2024-01-01', '2024-12-31'),
('2', 'E-commerce Platform', 'Building a scalable e-commerce platform for retail.', '2024-05-01', '2025-05-01'),
('3', 'Employee Management System', 'Implementing a new HR management system.', '2024-03-01', '2024-08-31'),
('4', 'Financial Forecasting', 'Developing a financial forecasting model.', '2024-06-01', '2024-11-30'),
('5', 'Inventory Management', 'Developing inventory control system.', '2024-02-15', '2025-02-15'),
('6', 'Cybersecurity Tools', 'Building cybersecurity monitoring tools.', '2024-04-10', '2024-12-31'),
('7', 'E-learning Platform', 'Designing an online learning platform.', '2024-09-01', '2025-08-31'),
('8', 'IoT Integration', 'Developing IoT applications for smart homes.', '2024-03-15', '2024-09-30'),
('9', 'Data Migration', 'Migrating data to a new cloud infrastructure.', '2024-07-01', '2024-12-01'),
('10', 'CRM Software', 'Building customer relationship management software.', '2024-04-15', '2025-01-15'),
('11', 'Market Research', 'Conducting market analysis for product launch.', '2024-05-15', '2024-10-15'),
('12', 'Blockchain Development', 'Building blockchain solutions for fintech.', '2024-01-20', '2024-12-20'),
('13', 'Smart City Solutions', 'Developing applications for smart cities.', '2024-06-10', '2025-01-10'),
('14', 'Machine Learning Framework', 'Creating a custom ML framework.', '2024-04-01', '2024-11-01'),
('15', 'Gaming Platform', 'Developing an online multiplayer gaming platform.', '2024-03-01', '2024-10-01'),
('16', 'Social Media Analytics', 'Analyzing trends on social media platforms.', '2024-02-15', '2024-07-15'),
('17', 'Energy Management', 'Building energy usage monitoring software.', '2024-03-20', '2025-03-20'),
('18', 'HR Automation', 'Automating HR processes for companies.', '2024-04-25', '2024-09-25'),
('19', 'E-voting System', 'Creating a secure online voting system.', '2024-07-01', '2024-12-01'),
('20', 'Mobile Banking App', 'Developing a mobile app for banking services.', '2024-06-15', '2025-06-15'),
('21', 'Cloud Migration', 'Moving legacy applications to the cloud.', '2024-02-10', '2024-09-10'),
('22', 'Logistics Tracking', 'Building real-time tracking for logistics.', '2024-03-01', '2024-12-01'),
('23', 'Virtual Reality', 'Developing VR apps for healthcare.', '2024-05-01', '2025-05-01'),
('24', 'Customer Support AI', 'Automating customer support using AI.', '2024-08-01', '2024-12-01'),
('25', 'Augmented Reality', 'Creating AR apps for retail shopping.', '2024-01-01', '2024-11-30');

INSERT INTO Meeting (MeetingID, EmployeeID, ProjectID, MeetingDate, MeetingTime) 
VALUES 
(1, 1, 1, '2024-11-15', '10:00:00'),
(2, 2, 2, '2024-11-15', '14:30:00'),
(3, 3, 3, '2024-11-14', '11:00:00'),
(4, 4, 1, '2024-11-13', '09:00:00'),
(5, 5, 4, '2024-11-16', '10:30:00'),
(6, 6, 5, '2024-11-16', '13:00:00'),
(7, 7, 6, '2024-11-17', '09:15:00'),
(8, 8, 7, '2024-11-17', '10:45:00'),
(9, 9, 8, '2024-11-18', '11:30:00'),
(10, 10, 9, '2024-11-19', '14:00:00'),
(11, 11, 10, '2024-11-20', '10:45:00'),
(12, 12, 11, '2024-11-21', '09:30:00'),
(13, 13, 12, '2024-11-21', '11:15:00'),
(14, 14, 13, '2024-11-22', '12:00:00'),
(15, 15, 14, '2024-11-23', '14:15:00'),
(16, 16, 15, '2024-11-24', '08:00:00'),
(17, 17, 16, '2024-11-25', '09:45:00'),
(18, 18, 17, '2024-11-26', '11:20:00'),
(19, 19, 18, '2024-11-27', '10:50:00'),
(20, 20, 19, '2024-11-27', '14:10:00'),
(21, 21, 20, '2024-11-28', '09:40:00'),
(22, 22, 21, '2024-11-28', '10:10:00'),
(23, 23, 22, '2024-11-29', '12:30:00'),
(24, 24, 23, '2024-11-30', '11:00:00'),
(25, 25, 24, '2024-12-01', '14:30:00');

DELIMITER //
CREATE TRIGGER prevent_duplicate_location
BEFORE INSERT ON Locations
FOR EACH ROW
BEGIN
    DECLARE location_exists INT;
    SELECT COUNT(*) INTO location_exists 
    FROM Locations 
    WHERE EmployeeID = NEW.EmployeeID 
    AND City = NEW.City 
    AND Country = NEW.Country
    AND Continent = NEW.Continent;
    IF location_exists > 0 THEN
        SIGNAL SQLSTATE '45000';
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE GetEmployeesByPosition()
BEGIN
    SELECT * FROM EMPLOYEE ORDER BY POSITION;
END //
DELIMITER ;

CREATE TABLE Roles (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(50) NOT NULL
);

INSERT INTO Roles (role_name) VALUES
('Admin'),
('Employee');

CREATE TABLE Users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

INSERT INTO Users (username, password) VALUES
('admin_user', 'admin_pass'),
('employee_user', 'employee_pass');

CREATE TABLE UserRoles (
    user_id INT,
    role_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (role_id) REFERENCES Roles(role_id),
    PRIMARY KEY (user_id, role_id)
);

INSERT INTO UserRoles (user_id, role_id) VALUES
((SELECT user_id FROM Users WHERE username = 'admin_user'), (SELECT role_id FROM Roles WHERE role_name = 'Admin')),
((SELECT user_id FROM Users WHERE username = 'employee_user'), (SELECT role_id FROM Roles WHERE role_name = 'Employee'));