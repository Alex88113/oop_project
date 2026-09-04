from loguru import logger


class Employee:
    """
    Class Employee for work with employees
    the class parent Employee with attributes in init constructor:
    name: name a employee
    salary: salary a employee
    """

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            logger.error("Name must be a string")
            raise ValueError("Name must be a string")

        if not value.strip():
            logger.error("field with a name employee is empty")
            raise ValueError("field with a name employee is empty")

        self._name = value

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """
        Method for validation a salary
        function take argument: value type float
        """
        if not isinstance(value, (float, int)):
            raise ValueError('salary is not invalid.')

        if not value:
            raise ValueError("field with a salary is empty")

        if value < 0:
            raise ValueError("salary is negative")

        self._salary = float(value)

    def __str__(self) -> str:
        return f"name employee: {self.name} | salary={self.salary}$"

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str) -> None:
        super().__init__(name, salary)
        self.department = department

    def __str__(self) -> str:
        """Переопределяем метод __str__ в классе наследнике"""
        return f"Manager Information: name={self.name} | salary={self.salary} | department={self.department}"


def main() -> None:
    try:
        employee_obj = Employee("Kirill", 39000.0)
        print(employee_obj)
        manager = Manager("Alex", 50.000, "jkdmks")
        print(manager)
    except ValueError as error:
        raise ValueError(f"transmitted arguments is not invalid: {error}.")
    except Exception as error:
        raise ValueError(f'An unknown error has occurred: {error}')


if __name__ == "__main__":
    main()
