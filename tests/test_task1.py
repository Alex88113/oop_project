import pytest

from base_oop.task1 import Person, Car


# Тестирование класса пользователя
class TestPersonClass:
    # подготавливаем данные для параметрических тестов
    @pytest.mark.parametrize("age, name, expected", [
        (19, "shura", 19),
        (12, "dima", 12),
        (45, "Anton", 45),
        (21, "Egor", 21)
    ])

    def test_age_person(self, name, age, expected) -> None:
        person = Person(age, name)
        assert person.age == expected

    # подготавливаем данные для параметрических тестов
    @pytest.mark.parametrize("age, name, expected", [
        (19, "shura", "shura"),
        (12, "dima", "dima"),
        (45, "Anton", "Anton"),
        (21, "Egor", "Egor")
    ])

    def test_person_name(self, name, age, expected):
        person = Person(age, name)
        assert person.name == expected


# Тестируем класс с машинами
class TestCarClass:
