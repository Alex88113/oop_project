from typing import Annotated

from classes_and_object.utils.logger import logger


class Courses:
    _students: Annotated[list[str], "список хранящий имена всех студентов"] = []
    _count_students: Annotated[int, "Количество студентов"] = 0

    def __init__(self, courses_name: str) -> None:
        self.courses_name = courses_name

    @property
    def courses_name(self) -> str:
        return self._courses_name

    @courses_name.setter
    def courses_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Student name is invalid.")

        if not value.strip():
            raise ValueError("field with a name is empty")

        if not 3 <= len(value) <= 15:
            raise ValueError("inappropriate name length a student.")

        self._courses_name = value

    @staticmethod
    def _valid_student_name(student_name: str) -> str:
        """
        Метод для валидации имени студента перед внесением его в список
        Если имя пройдет успешно все проверки то тогда, метод его вернет
        """
        if not isinstance(student_name, str):
            raise ValueError("Student name is invalid.")

        if not student_name:
            raise ValueError("field with a name is empty")

        if not 3 <= len(student_name) <= 15:
            raise ValueError("inappropriate name length a student.")

        return student_name.strip()

    @classmethod
    def add_student(cls, student_name: str) -> None:
        valid_student_name = cls._valid_student_name(student_name)
        cls._students.append(valid_student_name)
        cls._count_students += 1

    def drop_student(self, student_name: str) -> str | None:
        """
        Метод для отчисления студента
        parameters:
        student_name: имя студента которого хотим удалить из списка
        """
        valid_student_name = self._valid_student_name(student_name)
        for index, student in enumerate(self._students):
            if student == valid_student_name:
                delete_student = self._students.pop(index)
                return delete_student
        return None

    def print_all_students(self) -> None:
        """
        Проверяем не пустой ли список со студентами
        если пустой то, выводится сообщение и после выход из функции
        иначе выводим всех имеющихся студентов в из хранилища
        """
        if not self._students:
            logger.warning("List with students is empty.")
            return

        logger.info("------------ All Students ------------")
        for index, student in enumerate(self._students):
            logger.info(f"StudentID: {index} | name: {student}")
        logger.info(f"The total number of students is: {self._count_students}")
        logger.info("-" * 40)


def main() -> None:
    try:
        student1: Courses = Courses("alex")
        student2: Courses = Courses("Anton")
        student3: Courses = Courses("Anton")

        student1.add_student("Dima")
        student2.add_student("Kirill")
        student3.add_student("Masha")

        student3.print_all_students()
    except ValueError as error:
        logger.error("an error occurred with the input data: {}", error)
        raise
    except Exception as error:
        logger.error("an unexpected error has occurred: {}", error)
        raise


if __name__ == "__main__":
    main()
