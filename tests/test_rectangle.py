"""Модуль для тестирования класса Rectangle"""

import pytest

from base_oop.rectangle import Rectangle


class TestRectanle:
    """Тестирование класса вычисляющего площадь и периметр прямоуголника"""
    @pytest.mark.parametrize("length, width, expected_area, expected_perimeter", [
        # Квадраты
        (5.0, 5.0, 25.0, 20.0),
        (10.0, 10.0, 100.0, 40.0),
        (2.5, 2.5, 6.25, 10.0),

        # Прямоугольники с целыми числами
        (4.0, 6.0, 24.0, 20.0),
        (3.0, 7.0, 21.0, 20.0),
        (8.0, 12.0, 96.0, 40.0),
        (15.0, 20.0, 300.0, 70.0),

        # Прямоугольники с десятичными дробями
        (3.5, 4.2, 14.7, 15.4),
        (2.1, 5.7, 11.97, 15.6),
        (0.5, 0.3, 0.15, 1.6),
        (1.5, 2.5, 3.75, 8.0),

        # Очень маленькие значения
        (0.1, 0.1, 0.01, 0.4),
        (0.01, 0.02, 0.0002, 0.06),

        # Большие значения
        (1000.0, 2000.0, 2_000_000.0, 6000.0),
        (10_000.0, 5_000.0, 50_000_000.0, 30_000.0),

        # Разные соотношения сторон
        (1.0, 100.0, 100.0, 202.0),
        (0.5, 200.0, 100.0, 401.0),
        (2.0, 0.5, 1.0, 5.0),

        # Специальные случаи
        (1.0, 1.0, 1.0, 4.0),  # Единичный квадрат
        (0.0, 5.0, 0.0, 10.0),  # Нулевая длина
        (5.0, 0.0, 0.0, 10.0),  # Нулевая ширина
        (0.0, 0.0, 0.0, 0.0),   # Нулевые размеры
    ])

    def test_rectangle_calculations(self, length, width, expected_area, expected_perimeter):
        rectangle = Rectangle(length, width)
        area = rectangle.calculate_area()
        perimeter =  rectangle.calculate_perimeter()

        assert abs(area - expected_area) < 0.001
        assert abs(perimeter - expected_perimeter) < 0.0001

    @pytest.mark.parametrize("length, width, expected_error", [
        (-1.0, 5.0, "не может быть отрицательным"),
        (5.0, -3.0, "не может быть отрицательным"),
        (-1.0, -2.0, "не может быть отрицательным"),
        (-0.5, 10.0, "не может быть отрицательным"),
        (0.0, -5.0, "не может быть отрицательным"),
    ])

    def test_exception(self, length, width, expected_error):
        with pytest.raises(ValueError) as exc_info:
            Rectangle(length, width)
        assert expected_error in str(exc_info.value).lower()

    @pytest.mark.parametrize("length, width", [
        # Целые числа
        (5, 10),
        (3, 4),
        (7, 11),

        # Числа с плавающей точкой
        (3.14, 2.71),
        (1.618, 3.141),
        (0.577, 1.732),

        # Научная нотация
        (1e-3, 2e-3),
        (1e3, 2e3),
        (1.5e-2, 2.5e-2),
    ])

    def test_types_values(self, length, width):
        rectangle = Rectangle(length, width)
        assert rectangle.length == length
        assert rectangle.width == width

        assert isinstance(rectangle.calculate_area(), float)
        assert isinstance(rectangle.calculate_perimeter(), float)
