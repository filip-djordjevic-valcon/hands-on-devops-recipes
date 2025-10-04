from employee_manager import *

class FrontendManager:
    def __init__(self):
        self.EmployeeManager = EmployeeManager()

    def print_menu(self):
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Delete Employee by age")
        print("4. Update salary")
        print("5. Exit")

    def run(self):
        while True:
            self.print_menu()
            option = input("Please select an option: ")

            if option == "1":
                try:
                    name = input("Enter employee name: ")
                    age = int(input("Enter employee age: "))
                    salary = float(input("Enter employee salary: "))
                    self.EmployeeManager.add_employee(name, age, salary)
                except ValueError:
                    print("Error: Please enter valid numeric values for age and salary.")
            elif option == "2":
                self.EmployeeManager.list_employees()
            elif option == "3":
                try:
                    age_from = int(input("Enter the starting age of the employee to delete: "))
                    age_to = int(input("Enter the ending age of the employee to delete: "))
                    self.delete_employee_with_age(age_from, age_to)
                except ValueError:
                    print("Error: Please enter valid numeric values for age.")
            elif option == "4":
                try:
                    name = input("Enter the name of the employee to update salary: ")
                    new_salary = float(input("Enter the new salary: "))
                    self.EmployeeManager.update_employee_salary_by_name(name, new_salary)
                except ValueError:
                    print("Error: Please enter a valid numeric value for salary.")
            elif option == "5":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
