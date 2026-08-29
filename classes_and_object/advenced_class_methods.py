

class Employee:
    """
    Класс с работниками
    конструктор принимает параметры:
    name: имя сотрудника
    salary: его зарплата
    """
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Проверяем имя работника на валидность
        Return: возвращает корректное имя прошедшее все проверки
        Иначе выбрасывает exception
        """
        if not isinstance(value, str):
            raise ValueError("employee name is invalid")

        if not value.strip():
            raise ValueError("field with a name is empty")

        if not 3 <= len(value) <= 15:
            raise ValueError("the name length is not within the required range")

        self._name = value

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        """Является ли зарплата положительным числом"""
        return isinstance(salary, float | int) and salary >= 0

    @classmethod
    def from_string(cls, emp_str):
        try:
            name, salary_str = emp_str.split('-')
            salary = int(salary_str)

            if not cls.is_valid_salary(salary):
                raise ValueError(f"Invalid salary: {salary}")

            return cls(name, salary)

        except ValueError as e:
            print(f"Error creating employee from string '{emp_str}': {e}")
            return None

    def __str__(self) -> str:
        return f"Employee name: {self.name} | Salary: {self.salary}$"

def main() -> None:
    employee1 = Employee('Dima', -10000.000)
    empt1 = Employee.from_string("Bob-343434.434")

    print(str(employee1))
    print(employee1.is_valid_salary(employee1.salary))
    print(empt1)

main()