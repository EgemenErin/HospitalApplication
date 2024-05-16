import pickle
from datetime import date
from doctor import Doctor
from nurse import Nurse
from admin import Administrator

def login(username, password, employees):
    for employee in employees:
        if employee.username == username and employee.password == password:
            return employee
    return None

def schedule_on_call_duty(employees, person_name, duty_date):
    person = next((emp for emp in employees if emp.name == person_name), None)
    if not person:
        raise ValueError(f"Person {person_name} not found.")

    # Ensure only one doctor of a given specialization per day
    if isinstance(person, Doctor) and any(duty_date == duty.duty_date and isinstance(duty.person, Doctor) and duty.person.specialty == person.specialty for emp in employees for duty in emp.on_call_duties):
        raise ValueError(f"Doctor with the same specialization is already on duty on {duty_date}.")

    if isinstance(person, Doctor) or isinstance(person, Nurse):
        person.add_on_call_duty(duty_date)
    else:
        raise ValueError("Only doctors and nurses can have on-call duties.")

def print_on_call_schedule(employees):
    for emp in employees:
        if emp.on_call_duties:
            print(f"{emp.get_details()} On-Call Schedule:")
            for duty in emp.on_call_duties:
                print(f"  {duty}")

def main():
    try:
        with open('employees.pkl', 'rb') as file:
            employees = pickle.load(file)
    except FileNotFoundError:
        employees = []
    except Exception as e:
        print(f"An error occurred: {e}")
        employees = []

    # Create sample users and add them to the employees list
    Egemen = Administrator("Egemen", "Erin", "3131", "Egemen", "12345")
    Toprak = Doctor("Toprak", "Solombay", "1234", "5678", "Toprak", "Cardiologist", "31")
    employees.append(Egemen)
    employees.append(Toprak)

    username = input("Enter username: ")
    password = input("Enter password: ")
    user = login(username, password, employees)

    if not user:
        print("Invalid credentials!")
        return

    if isinstance(user, Doctor) or isinstance(user, Nurse):
        print("Doctors and Nurses View")
        for emp in employees:
            if isinstance(emp, Doctor) or isinstance(emp, Nurse):
                print(emp.get_details())
        person_name = input("Enter the name of the person to see their schedule: ")
        person = next((emp for emp in employees if emp.name == person_name), None)
        if person:
            print(person.on_call_duties)
        else:
            print("Person not found.")
    elif isinstance(user, Administrator):
        print("Administrator View")
        while True:
            action = input("Enter action (view, schedule, add, edit, exit): ")
            if action == "view":
                print_on_call_schedule(employees)
            elif action == "schedule":
                person_name = input("Enter the name of the person to schedule: ")
                try:
                    duty_date = date.fromisoformat(input("Enter the duty date (YYYY-MM-DD): "))
                    schedule_on_call_duty(employees, person_name, duty_date)
                except ValueError as e:
                    print(e)
            elif action == "add":
                # Add new user logic here
                pass
            elif action == "edit":
                # Edit user data logic here
                pass
            elif action == "exit":
                break

    with open('employees.pkl', 'wb') as file:
        pickle.dump(employees, file)

if __name__ == "__main__":
    main()
