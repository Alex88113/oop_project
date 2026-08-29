"""
Модуль для тестирования класса Employee
"""

import pytest

from classes_and_object.advenced_class_methods import Employee


class TestEmployee:
    # Тест с корректными данными
    @pytest.mark.parametrize("name, salary, expected", [
        ("Alex", 10000.990, 10000.990),
        ('Dima', 90.000, 90.000),
        ('Anton', 78000.0, 78000.0),
        ('Egor', 56.9000, 56.9000)
    ])

    def test_salary(self, name: str, salary: float, expected: float) -> None:
        employee = Employee(name, salary)
        assert employee.salary == expected
        assert isinstance(employee.salary, float)
        assert employee.salary > 0

        
    @pytest.mark.parametrize("invalid_name, invalid_salary", [
        ('', -23),
        (None, True),
        (0, ''),
        (-3232, '   '),
        (None, False),
        (0, 'dw3')
    ])
    
    def test_raises_exception(self, invalid_name, invalid_salary) -> None:
        with pytest.raises(ValueError):
            Employee(invalid_name, invalid_salary)

    @pytest.mark.parametrize("salary, expected", [
        (10.343, True),
        (333.343, True),
        (343.43, True),
        (43534.34, True)
    ])

    def test_is_valid_salary(self, salary: float, expected: bool) -> None:
        assert Employee.is_valid_salary(salary) == expected

    @pytest.mark.parametrize("invalid_salary, invalid_result",[
        ('32323', False),
        (-12.43, False),
        (' ', False),
        (-34343, False),
        (None, False),
        ('     ', False)
    ])

    def test_negative_scenarios(self, invalid_salary, invalid_result) -> None:
        assert Employee.is_valid_salary(invalid_salary) == invalid_result
