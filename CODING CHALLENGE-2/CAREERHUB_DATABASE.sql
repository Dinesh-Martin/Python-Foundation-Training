create database careerhub2
use careerhub2

IF OBJECT_ID('Applications', 'U') IS NOT NULL DROP TABLE Applications;
IF OBJECT_ID('Jobs', 'U') IS NOT NULL DROP TABLE Jobs;
IF OBJECT_ID('Applicants', 'U') IS NOT NULL DROP TABLE Applicants;
IF OBJECT_ID('Companies', 'U') IS NOT NULL DROP TABLE Companies;


CREATE TABLE Companies (
    CompanyID INT PRIMARY KEY,
    CompanyName NVARCHAR(255) NOT NULL,
    Location NVARCHAR(255)
);


CREATE TABLE Jobs (
    JobID INT PRIMARY KEY,
    CompanyID INT NOT NULL,
    JobTitle NVARCHAR(255) NOT NULL,
    JobDescription TEXT,
    JobLocation NVARCHAR(255),
    Salary DECIMAL(18, 2) CHECK (Salary >= 0),
    JobType NVARCHAR(50),
    PostedDate DATETIME,
    FOREIGN KEY (CompanyID) REFERENCES Companies(CompanyID)
);


CREATE TABLE Applicants (
    ApplicantID INT PRIMARY KEY,
    FirstName NVARCHAR(255),
    LastName NVARCHAR(255),
    Email NVARCHAR(255),
    Phone NVARCHAR(20),
    Resume TEXT
);


CREATE TABLE Applications (
    ApplicationID INT PRIMARY KEY,
    JobID INT NOT NULL,
    ApplicantID INT NOT NULL,
    ApplicationDate DATETIME,
    CoverLetter TEXT,
    FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
    FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
);


INSERT INTO Companies VALUES
(1, 'TechNova Inc.', 'New York'),
(2, 'DataWave Solutions', 'San Francisco'),
(3, 'CloudCraft', 'Austin'),
(4, 'CyberCore Ltd.', 'Chicago'),
(5, 'NeuralNet AI', 'Boston');


INSERT INTO Jobs VALUES
(101, 1, 'Software Engineer', 'Develop scalable applications.', 'New York', 95000, 'Full-time', GETDATE()),
(102, 2, 'Data Analyst', 'Analyze big data sets.', 'San Francisco', 85000, 'Full-time', GETDATE()),
(103, 3, 'DevOps Engineer', 'Manage cloud infrastructure.', 'Austin', 92000, 'Contract', GETDATE()),
(104, 4, 'Cybersecurity Specialist', 'Monitor security incidents.', 'Chicago', 98000, 'Full-time', GETDATE()),
(105, 5, 'AI Researcher', 'Work on deep learning models.', 'Boston', 110000, 'Full-time', GETDATE());


INSERT INTO Applicants VALUES
(201, 'Alice', 'Johnson', 'alice.johnson@example.com', '1234567890', 'Resume_Alice.pdf'),
(202, 'Bob', 'Smith', 'bob.smith@example.com', '2345678901', 'Resume_Bob.pdf'),
(203, 'Charlie', 'Lee', 'charlie.lee@example.com', '3456789012', 'Resume_Charlie.pdf'),
(204, 'Diana', 'Ross', 'diana.ross@example.com', '4567890123', 'Resume_Diana.pdf'),
(205, 'Ethan', 'Wright', 'ethan.wright@example.com', '5678901234', 'Resume_Ethan.pdf');


INSERT INTO Applications VALUES
(301, 101, 201, GETDATE(), 'I am excited to join your team!'),
(302, 102, 202, GETDATE(), 'Experienced in data visualization and analytics.'),
(303, 103, 203, GETDATE(), 'Ready to work in DevOps environments.'),
(304, 104, 204, GETDATE(), 'Skilled in cybersecurity and threat analysis.'),
(305, 105, 205, GETDATE(), 'Passionate about AI and neural networks.');

select * from Applicants
