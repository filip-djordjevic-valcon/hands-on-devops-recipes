class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"Employee is set: name = {self.name}, age = {self.age}, salary = {self.salary}"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 18 or value > 60:
            raise ValueError("Age must be between 18 and 60")
        self._age = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 500 or value > 10000:
            raise ValueError("Salary must be between 500 and 10000")
        self._salary = value