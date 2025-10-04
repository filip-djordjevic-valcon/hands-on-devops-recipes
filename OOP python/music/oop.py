class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Name cannot be empty")
        if not house:
            raise ValueError("House cannot be empty")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    #print (f"Hello {student.name}, you are from {student.house}")
    print (student)

def get_student():
    name = input("Enter your name: ")
    house = input("Enter your house: ")
    try: 
        return Student(name, house)
    except ValueError:
        ...

if __name__ == "__main__":
    main() 