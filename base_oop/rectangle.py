from typing import Annotated

from base_oop.utils.logger import *

__all__ = ["logger"]

type VALUE_PARAMETERS = Annotated[float, "тип данных для параметров конструктора класса Rectangle"]

# Объявляем класс Rectangle для вычисления площади и периметра прямоугольника
class Rectangle:
    def __init__(
            self,
            length: VALUE_PARAMETERS,
            width: VALUE_PARAMETERS
    )-> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.length)


rectangle: Rectangle = Rectangle(121.21, 434.43)

logger.debug("Площадь: {}", rectangle.calculate_area())
logger.debug("Периметр: {}", rectangle.calculate_perimeter())
