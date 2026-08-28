"""Тестирование системы студентов"""

import pytest

from classes_and_object.student_system import Courses


class TestCourses:
    """Тестируем обычные случаи"""
    @pytest.mark.parametrize("name, expected", [
        ('Alex', 'Alex'),
        ('Dima', 'Dima'),
        ('Anton', 'Anton'),
        ('Kirill', 'Kirill')
    ])

    def test_courses_name(self, name: str, expected: str) -> None:
        assert Courses(name).courses_name == expected


    # Проверка исключений
    @pytest.mark.parametrize("invalid_name", [
        None,
        1,
        323,
        True,
        False,
        "",  # Пустая строка
        "   ",  # Только пробелы
    ])

    def test_raises_value(self, invalid_name) -> None:
        with pytest.raises(ValueError):
            Courses(courses_name=invalid_name)


    def test_types_data(self) -> None:
        courses = Courses('Alex')
        assert isinstance(courses.courses_name, str)
        assert len(courses.courses_name) >= 3