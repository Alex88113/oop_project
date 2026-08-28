from base_oop.utils.logger import *

__all__ = ['logger']

class BankAccount:
    """Банковский класс для совершения банковских операций"""

    def __init__(self, account_number: str, balance: float=0.0) -> None:
        self.account_number = account_number
        self.balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        """
        Проверяем входные данные
        перед внесением значения в атрибут self._balance
        Args:
            value (float): _description_
        """
        if not isinstance(value, (int, float)):
            logger.error("значение невалидно")
            raise

        if value <= 0:
            logger.error("Сумма пополнения отрицательна либо равна 0")
            raise

        self._balance = value

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, float | int):
            raise ValueError("Тип суммы некорректен")

        if amount <= 0:
            logger.error("Сумма пополнения отрицательна либо равна 0")
            raise

        self._balance += amount
        logger.info("Баланс пополнен на: {:.2f} руб.", self._balance)
        return self._balance

    def withdrawal(self, amount: float) -> None:
        if self.balance <= 0:
            raise ValueError("Средств на балансе нет.")
        if amount <= 0:
            raise ValueError("Сумма снятия отрицательна либо равна 0")

        self.balance -= amount
        logger.debug("Снято: {} рублей", amount)

    def __str__(self) -> str:
        return f"Accout number: {self.account_number} | balance={self.balance} рублей."

def main() -> None:
    try:
        bank_account: BankAccount = BankAccount("343434 32323 32323 32312", 343.34)
        bank_account.deposit(223.323)
        logger.info("Текущий баланс: {}", bank_account.balance)
        bank_account.withdrawal(100.0)
    except ValueError as error:
        logger.error("Переданные некорректные значения в параметры конструктора: {}", error)
        raise
    except Exception as error:
        logger.error("Возникла неизвестная ошибка: {}", error)
        raise

# ЗАПУСК
if __name__ == "__main__":
    main()
