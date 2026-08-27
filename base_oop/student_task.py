from typing import Annotated

type LIST_GRADES = Annotated[list[float | int], 'Список с оценками студента']

# Класс для работы со студентами
class Student:
    def __init__(
            self,
            name: str,
            age: int,
            group: Annotated[str, "Название группы"],
            grades: LIST_GRADES
    ) -> None:
        self.name = name
        self.age = age
        self.group = group
        self.grades = grades

    # Вычисляем средний балл студента из всего списка с его оценками
    def calculate_average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

    # Валидируем новый балл который будем добавлять в список с остальными оценками
    @staticmethod
    def _validation_grade(grade: float | int) -> float | int:
        if not isinstance(grade, float | int):
            raise ValueError('grade is not valid')
        if grade <= 0:
            raise ValueError("the score is negative or equal to 0")
        if not 2 <= grade <= 5:
            raise ValueError("the score is not in the right range")
        return grade

    # добавляем проверенный балл в список
    def add_grade(self, grade: float) -> None:
        valid_grade = self._validation_grade(grade)
        self.grades.append(valid_grade)

    # метод печатающий информацию об студенте
    def print_info_student(self) -> None:
        print(f'name: {self.name} | age: {self.age} | group: {self.group} | grades: {self.grades}')

# точка входа
def main() -> None:
    student1 = Student(
        'shura',
        19,
        'РПО-3',
        [2.4, 5, 3.6, 4.1, 5]
    )
    average_grade = student1.calculate_average_grade()
    print(f'Grade average: {average_grade:.2f}')
    student1.add_grade(5)
    student1.print_info_student()

# ПУСК
if __name__ == "__main__":
    main()