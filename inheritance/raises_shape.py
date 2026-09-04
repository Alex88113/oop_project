import math


class Shape:
    @staticmethod
    def area(value: float) -> float:
        raise NotImplementedError("Вызвано исключение из класса Shape")

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self._area: float | None = None

    @property
    def area(self) -> float:
        return float(math.pi * self.radius ** 2)

class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length
        self._area: float | None = None

    @property
    def area(self) -> float:
        return float(self.length * self.length)

shapes = (Circle(32332), Square(32323))
for shape in shapes:
    print(shape.area)
