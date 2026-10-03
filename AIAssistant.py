
class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Зарплата: {self.salary} грн")



class Developer(Employee):
    def __init__(self, name: str, age: int, salary: float, programming_language: str):

        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display_language(self):
        print(f"Мова програмування: {self.programming_language}")



class Manager(Employee):
    def __init__(self, name: str, age: int, salary: float, team_size: int):

        super().__init__(name, age, salary)
        self.team_size = team_size

    def display_team_size(self):
        print(f"Розмір команди: {self.team_size} осіб")





dev = Developer(name="Олексій", age=25, salary=80000, programming_language="Python")
print("--- Інформація про Розробника ---")
dev.display_employee_info()
dev.display_language()

print()


dev = Developer(name="Олексій", age=25, salary=80000, programming_language="Python")
print("--- Інформація про Розробника ---")
dev.display_employee_info()
dev.display_language()
