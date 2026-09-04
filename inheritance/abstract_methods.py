import math
import logging

logging.basicConfig(
    filename='logs/app.log',
    format="%(levelname)s - %(asctime)s - %(message)s",
    level=logging.DEBUG,
    encoding='utf-8'
)

class Shape:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> None:
        raise  NotImplementedError("Вызвано исключение из класса Shape")

class Circle(Shape):
    def __init__(self, width, height, radius: float) -> None:
        super().__init__(width,  height)
        self.radius = radius

    @property
    def area(self) -> float:
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height, length_base: float) -> None:
        super().__init__(width,  height)
        self.length_base = length_base

    @property
    def area(self) -> float:
        if not self.length_base <= 0 or self.height <= 0:
            return (self.length_base * self.height) / 2
        else:
            raise ValueError("Такой фигуры нет.")

list_shapes: list = [
    Circle(121.212, 212.23, 323.32),
    Rectangle(2323.323, 32.33, 32.53)
]
results = (shape for shape in list_shapes)
for shape in results:
    logging.debug(shape.area)