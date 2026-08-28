from base_oop.utils.logger import *

__all__ = ["logger"]


class User:
    def __init__(self, name: str, age: int, email: str) -> None:
        self._name = name
        self._age = age
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            logger.error("username is invalid")
            raise
        if not value.strip():
            logger.error("field with a name is empty")
            raise
        if not 3 <= len(value) <= 20:
            logger.error("Неподходяшщая длина имени")
            raise
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int):
            logger.error("age is invalid.")
            raise
        if value <= 0:
            logger.error("age is negative or equal to zero")
            raise
        if not 16 <= value <= 100:
            logger.error("the age is not in the right range")
            raise
        self._age = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if not isinstance(value, str):
            logger.error("email is invalid.")
            raise
        if not value.strip():
            logger.error("field with a email is empty")
            raise
        if "@" not in value or "." not in value:
            logger.error("email не содержит специальных символов и '.'")
            raise
        self._email = value

    def __str__(self) -> str:
        return f"Username: {self._name} | age: {self._age} | email: {self._email}"

    def __repr__(self) -> str:
        return f"User(name={self._name}, age={self._age}, email={self._email})"


def main() -> None:
    try:
        user1 = User("Anton", 19, "sanya.kucheryavvkhbk.ru")
        user1.name = "Shura"
        user1.email = "sanya.kucheryavvkhbk@.ru"
        logger.debug(str(user1))
    except ValueError as error:
        logger.error("Некорректно указанные аргументы: {}", error)
        raise
    except Exception as error:
        logger.error("An unknown error has occured: {}", error)
        raise


if __name__ == "__main__":
    main()
