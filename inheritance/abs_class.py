import math
from abc import ABC, abstractmethod

from loguru import logger


class Shape(ABC):
    def __init__(self, color) -> None:
        self.color = color

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    def describe(self) -> str:
        return f"This is a {self.color} {self.__class__.__name__.lower()}"

class Circle(Shape):
    def __init__(self, color, radius: float | int) -> None:
        super().__init__(color)
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, color, width: float, height: float) -> None:
        super().__init__(color)
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

def main() -> None:
    circle = Circle("red", 332.23)
    rectangle = Rectangle("yellow", 232.32, 32.2)

    logger.debug("Площадь круга равна = {:.2f}см.", circle.calculate_area())
    logger.debug('Периметр круга равен: {:.2f}см.', circle.calculate_perimeter())
    logger.debug("Площадь прямоугольник равна = {:.2f}см.", rectangle.calculate_area())
    logger.debug("Периметр прямоугольника составляет: {}см", rectangle.calculate_perimeter())


if __name__ == "__main__":
    main()