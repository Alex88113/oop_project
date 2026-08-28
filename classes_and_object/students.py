from typing import Annotated

from classes_and_object.shames.student_shame import Student, students


class StudentManager:
    """Класс StudentManager для управления и работы со студенами"""
    _students: Annotated[list[Student], "list with students"] = []

    @classmethod
    def add_student(cls, student: Student) -> None:
        if not student in cls._students:
            cls._students.append(student)
        return None

    @staticmethod
    def _validation_find_id(student_id: int) -> int:
        """Проверяем поисковой id на корректность а после возвращаем его
        student_id: Сам поиской ID
        Return после успешного прохождения всех проверок возвращаем проверенный ID
        """
        
        if not isinstance(student_id, int):
            raise ValueError("find a id is invalid.")
        
        if student_id <= 0:
            raise ValueError("ID is negative or equal to zero")
        
        if student_id > 15:
            raise ValueError("Превышен поисковой ID")

        return student_id

    def find_student_by_id(self, student_id: int) -> Student | None:
        """Метод для поиска студента по цифровому идентификатору
        
        student_id поисковой ID
        
        Return возвращаем найденого студента в виде Student модели
        
        если студента по такому id нет возвращается None
        
        """
        for student in self._students:
            if student.student_id == self._validation_find_id(student_id):
                return Student(
                    student_id=student.student_id,
                    fullname=student.fullname,
                    group=student.group,
                    age=student.age,
                    name=student.name,
                )
        return None

    def delete_student(self, student_id: int) -> None:
        """Метод для удаления найдено студента по ID
        self._validation_find_id(student_id) получаем валидный ID
        """
        valid_id = self._validation_find_id(student_id)
        for index, student in enumerate(self._students):
            if student.student_id == valid_id:
                remove_student = self._students.pop(index)
                print(f"Delete a student: {remove_student}")
                return
        return None

    def print_all_students(self) -> None:
        """Проверяем не пустое ли хранилище со студентами"""
        
        if not self._students:
            print("list with students is empty")
        
        """Если не пустое то, выводим информацию обо всех учащихся"""
        
        for student in self._students:
            print(
                f"StudentID: {student.student_id} | fullname: {student.fullname} | age: {student.age} | group={student.group}"
            )


# Точка входа в программу
def main() -> None:
    add_students = (Student(**student) for student in students)
    manager = StudentManager()
    for student in add_students:
        manager.add_student(student)

    manager.find_student_by_id(2)
    manager.delete_student(1)


# Стартуем
if __name__ == "__main__":
    main()
