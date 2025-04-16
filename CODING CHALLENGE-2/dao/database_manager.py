import pyodbc
from util.db_conn_util import get_connection
from exception.database_connection_exception import DatabaseConnectionException
from exception.negative_salary_exception import NegativeSalaryException

def initialize_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("IF OBJECT_ID('Applications', 'U') IS NOT NULL DROP TABLE Applications")
        cursor.execute("IF OBJECT_ID('Jobs', 'U') IS NOT NULL DROP TABLE Jobs")
        cursor.execute("IF OBJECT_ID('Applicants', 'U') IS NOT NULL DROP TABLE Applicants")
        cursor.execute("IF OBJECT_ID('Companies', 'U') IS NOT NULL DROP TABLE Companies")
        cursor.execute("""
        CREATE TABLE Companies (
            CompanyID INT PRIMARY KEY,
            CompanyName NVARCHAR(255),
            Location NVARCHAR(255)
        );
        CREATE TABLE Jobs (
            JobID INT PRIMARY KEY,
            CompanyID INT,
            JobTitle NVARCHAR(255),
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
            JobID INT,
            ApplicantID INT,
            ApplicationDate DATETIME,
            CoverLetter TEXT,
            FOREIGN KEY (JobID) REFERENCES Jobs(JobID),
            FOREIGN KEY (ApplicantID) REFERENCES Applicants(ApplicantID)
        );
        """)
        conn.commit()
        conn.close()
    except pyodbc.Error as e:
        raise DatabaseConnectionException(str(e))

def insert_company(company_id, name, location):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Companies VALUES (?, ?, ?)", (company_id, name, location))
    conn.commit()
    conn.close()

def insert_job(job_id, company_id, title, description, location, salary, job_type, posted_date):
    if salary < 0:
        raise NegativeSalaryException()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Jobs VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                   (job_id, company_id, title, description, location, salary, job_type, posted_date))
    conn.commit()
    conn.close()

def insert_applicant(applicant_id, first_name, last_name, email, phone, resume):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Applicants VALUES (?, ?, ?, ?, ?, ?)",
                   (applicant_id, first_name, last_name, email, phone, resume))
    conn.commit()
    conn.close()

def insert_application(app_id, job_id, applicant_id, application_date, cover_letter):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Applications VALUES (?, ?, ?, ?, ?)",
                   (app_id, job_id, applicant_id, application_date, cover_letter))
    conn.commit()
    conn.close()

def get_jobs_by_salary_range(min_salary, max_salary):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT JobTitle, CompanyID, Salary FROM Jobs WHERE Salary BETWEEN ? AND ?", 
                   (min_salary, max_salary))
    return cursor.fetchall()

def get_all_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Jobs")
    return cursor.fetchall()

def get_all_companies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Companies")
    return cursor.fetchall()

def get_all_applicants():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Applicants")
    return cursor.fetchall()

def get_applications_for_job(job_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Applications WHERE JobID = ?", (job_id,))
    return cursor.fetchall()
