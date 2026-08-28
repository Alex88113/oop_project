from typing import Annotated

from loguru import logger


# Объявляем класс Person
class Person:
    """Создаем конструктор __init__ внутри которого задаём атрибуты: name, age
    После присваиваем атрибутам значение параметров
    """
    def __init__(
            self,
            age: Annotated[int, 'age a user'],
            name: Annotated[str, "Username"]
    ) -> None:
        self.age = age
        self.name = name

    # метод для приветствия с пользователем
    def greet(self) -> str:
        return f"Hi, my name is {self.name}"

# создаем экземпляр класса Person
person1: Person = Person(19, 'Shura')
logger.debug('Name: {} | Age: {}', person1.name, person1.age)
logger.debug(person1.greet())


type CAR_OBJ = Annotated[Car, "Класс с данными машин"]

# Определяем класс Car с атрибутами: марка, модель и год выпуска
class Car:
    def __init__(
            self,
            stamp: Annotated[str, "Марка машины"],
            model: str,
            year_of_release: Annotated[int, "Год выпуска"]
    ) -> None:
        self.stamp = stamp
        self.model = model
        self.year_of_release = year_of_release

    def display_info(self) -> None:
        logger.debug("Stamp: {} | Model: {} | Year_of_release: {}", self.stamp, self.model, self.year_of_release)


bmw: CAR_OBJ = Car("BMW", 'X15', 2000)

logger.debug("Model: {}", bmw.model)
logger.debug("Stamp: {}", bmw.stamp)
logger.debug("Year: {}", bmw.year_of_release)
bmw.display_info()
