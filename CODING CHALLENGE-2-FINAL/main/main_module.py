from dao.database_manager import *
from exception.invalid_email_exception import InvalidEmailException
from exception.negative_salary_exception import NegativeSalaryException
import re
from datetime import datetime

def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise InvalidEmailException()

def main():
    print("CareerHub Job Board")
    job_list = []  # in-memory list of jobs
    applicant_list = []  # in-memory list of applicants

    while True:
        print("\nMenu:")
        print("1. Initialize Database")
        print("2. Add Company")
        print("3. Add Job Listing")
        print("4. Add Applicant")
        print("5. Apply for Job")
        print("6. View All Jobs")
        print("7. View Jobs in Salary Range (from list)")
        print("8. View All Applicants")
        print("9. View Applications for Job")
        print("10. Refresh Cache (jobs & applicants)")
        print("0. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                initialize_database()
                print("Database initialized.")
            elif choice == "2":
                cid = int(input("Company ID: "))
                name = input("Company Name: ")
                location = input("Location: ")
                insert_company(cid, name, location)
                print("Company added.")
            elif choice == "3":
                jid = int(input("Job ID: "))
                cid = int(input("Company ID: "))
                title = input("Job Title: ")
                desc = input("Description: ")
                loc = input("Location: ")
                salary = float(input("Salary: "))
                jtype = input("Job Type: ")
                date = datetime.now()
                insert_job(jid, cid, title, desc, loc, salary, jtype, date)
                print("Job listing added.")
            elif choice == "4":
                aid = int(input("Applicant ID: "))
                fname = input("First Name: ")
                lname = input("Last Name: ")
                email = input("Email: ")
                validate_email(email)
                phone = input("Phone: ")
                resume = input("Resume filename: ")
                insert_applicant(aid, fname, lname, email, phone, resume)
                print("Applicant profile created.")
            elif choice == "5":
                appid = int(input("Application ID: "))
                jobid = int(input("Job ID: "))
                aid = int(input("Applicant ID: "))
                date = datetime.now()
                cover = input("Cover Letter: ")
                insert_application(appid, jobid, aid, date, cover)
                print("Application submitted.")
            elif choice == "6":
                for job in job_list:
                    print(job)
            elif choice == "7":
                min_sal = float(input("Min Salary: "))
                max_sal = float(input("Max Salary: "))
                filtered = [job for job in job_list if min_sal <= job[5] <= max_sal]
                for job in filtered:
                    print(job)
            elif choice == "8":
                for app in applicant_list:
                    print(app)
            elif choice == "9":
                jobid = int(input("Enter Job ID: "))
                applications = get_applications_for_job(jobid)
                for a in applications:
                    print(a)
            elif choice == "10":
                job_list.clear()
                job_list.extend(get_all_jobs())
                applicant_list.clear()
                applicant_list.extend(get_all_applicants())
                print("In-memory cache updated.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
