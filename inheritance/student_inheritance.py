from loguru import logger

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Student name: {self.name}, age={self.age} years"

class StudentManager(Student):
    def __init__(self, name, age, student_id: int) -> None:
        """
        super() function это функция обеспечивающая доступ к методам и атрибутам родительского класса из наследников
        :param name:
        :param age:
        :param student_id:
        """
        super().__init__(name, age)
        self.student_id = student_id
        self._grades: list[int | float] = []

    @staticmethod
    def _validation_grade(grade: float | int) -> float | int:
        if isinstance(grade, (float, int)) and 2 <= grade <= 5:
            return grade
        else:
            logger.error("grade is not invalid or is negative")
            raise

    def add_grade(self, grade: float | int) -> None:
        valid_grade = self._validation_grade(grade)
        self._grades.append(valid_grade)
        print(f'grade {valid_grade} is adding in grades list')

    def __str__(self) -> str:
        return f"StudentID: {self.student_id} | name: {self.name} | age={self.age} | grades: {self._grades}"

manager = StudentManager("Alex", 19, 1)
manager.add_grade(2)
print(str(manager))