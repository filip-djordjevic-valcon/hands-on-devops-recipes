from employee import *

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, salary):
        print ("Enter employee data: ")
        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if (len(self.employees) == 0):
            print("No employees found.")
            return
        else:
            for emp in self.employees:
                print(emp) 

    def delete_employee_with_age(self, age_from, age_to):
        if (len(self.employees) == 0) or not (18 <= age_from <= 60 and 18 <= age_to <= 60):
            if len(self.employees) == 0:
                print("No employees found.")
            if not (18 <= age_from <= 60 and 18 <= age_to <= 60):
                print("Error: Age must be between 18 and 60.")
            return
        else:
            found = False
            for emp in self.employees:
                if emp.age >= age_from and emp.age <= age_to:
                    self.employees.remove(emp)
                    print(f"Deleted employee: {emp}")
                    fount = True

            if not found:
                print(f"No employees found with age between {age_from} and {age_to}.")
            else:
                print(f"Employees with age between {age_from} and {age_to} have been deleted.")
            

    def find_employee_by_name(self, name):
        if (len(self.employees) == 0):
            print("No employees found.")
            return
        else:
            for emp in self.employees:
                if emp.name == name:
                    print(f"Found employee: {emp}")
                    return
            print(f"No employee found with name: {name}")

    def update_employee_salary_by_name(self, name, new_salary):
        for emp in self.employees:
            if emp.name == name:
                emp.salary = new_salary
                print(f"Updated salary for employee: {emp}")
                return
        print(f"No employee found with name: {name}")

    def employee_exists(self, name):
        for emp in self.employees:
            if emp.name == name:
                return True
        return False
    
    def get_length(self):
        return len(self.employees)