class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f"name: {self.name} | salary={self.salary}"

    def __repr__(self) -> str:
        return f"Employee(name={self.name}, salary={self.salary})"


class EmployeeManager(Employee):
    def __init__(self, name, salary, employee_id: int, age: int) -> None:
        super().__init__(name, salary)
        self.employee_id = employee_id
        self.age = age

    def __str__(self) -> str:
        return f"Employee ID: {self.employee_id} | name: {self.name} | salary={self.salary} | age: {self.age}"

    def __repr__(self) -> str:
        return f"Employee(name={self.name}, salary={self.salary} | employee_id: {self.employee_id} | age: {self.age})"

emp = EmployeeManager('dmitriy', 100000.000, 1, 19)
print(emp)