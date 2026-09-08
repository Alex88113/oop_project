from classes_and_object.utils.logger import logger


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def age(self) -> int:
        return self._age
    
    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            logger.error("Имя не является строкой")
            raise TypeError("Имя не является строкой")
        
        clear_value: str = value.strip()
        
        if not clear_value:
            logger.error("поле с именем пустое")
            raise ValueError("поле с именем пустое") # field with a name is empty
        
        if not 3 <= len(clear_value) <= 15:
            logger.error(f"Длина имени юзера от 3 - 15 символов, а у вас всего: {len(value)}")
            raise ValueError(f"Длина имени юзера от 3 - 15 символов, а у вас всего: {len(value)}")
        
        self._name = clear_value
        
        
    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            logger.error("Возраст необходим в виде целого числа")
            raise TypeError("Возраст необходим в виде целого числа")
        
        if not 16 <= value <= 120:
            logger.error("Возраст вне диапазона 16 - 120 лет")
            raise ValueError("Возраст вне диапазона 16 - 120 лет")
        
        self._age = value
        
    def __str__(self) -> str:
        return f"Person name: {self._name} | age={self._age}"
    
    def __repr__(self) -> str:
        return f"Person(name={self._name}, age={self._age})"


def main() -> None:
    try:
        person1 = Person("Dima", 19)
        person1.name = "007"
        person1.age = 19
        
        logger.info(person1.name)
        logger.info(person1.age) 
        logger.info(str(person1))
        logger.debug(repr(person1))
    except ValueError as error:
        logger.error(f"Неверно переданные аргументы в параметрах: {error}")
        raise
    except TypeError as error:
        logger.error(f"Переданны аргументы неподходяшщего типа: {error}")
        raise
    except Exception as error:
        logger.error(f"Возникла неизвесная ошибка: {error}")
        raise

if __name__ == "__main__":
    main()
