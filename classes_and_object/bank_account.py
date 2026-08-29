from classes_and_object.utils.logger import *

__all__ = ['logger']

class BankAccount:
    """
    Банковский класс для совершения банковских операций
    конструктор принимает параметры:
    account_name: ник банковского аккаунта
    balance: баланс пользователя
    """

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
        logger.info("the balances is topped up on: {:.2f} руб.", self._balance)
        return self._balance

    @staticmethod
    def _validation_withdrawal_amounts(amount: float) -> float:
        """
        Метод для валидаци суммы снятия средств со счета
        метод принимает параметр:
        amount: сумма снятия
        
        Return  возвращает корректное значения типа (float), прошедшее успешно все проверки
        В противном случае выбрасывается исключение
        """
        if not isinstance(amount, float | int):
            raise ValueError("withdrawal amount is not invalid.")
        
        if not amount:
            raise ValueError("field with a withdrawal amount is empty")
        
        if amount <= 0:
            raise ValueError("The withdrawal amount is negative or equal to zero")
        
        return amount
    
    def withdrawal(self, amount: float) -> None:
        """
        Метод для снятия средств
        принимает параметр amount: сумма которую хотим снять со счета
        """
        # сперва проверяем есть ли, на нашем балансе средства для снятия
        if self.balance <= 0:
            raise ValueError("dont have money on the balance.")
        
        get_valid_amount: float = self._validation_withdrawal_amounts(amount)
        self.balance -= get_valid_amount
        logger.debug("funds withdrawn: {}$", get_valid_amount)

    def __str__(self) -> str:
        return f"Account number: {self.account_number} | balance={self.balance} рублей."

# ТОЧКА ВХОДА
def main() -> None:
    try:
        bank_account: BankAccount = BankAccount("343434 32323 32323 32312", 343.34)
        bank_account.deposit(223.323)
        logger.info("Текущий баланс: {}", bank_account.balance)
        bank_account.withdrawal(-100.0)
        logger.info("Сумма после снятия составляет: {}", bank_account.balance)
    except ValueError as error:
        logger.error("Переданные некорректные значения в параметры конструктора: {}", error)
        raise
    except Exception as error:
        logger.error("Возникла неизвестная ошибка: {}", error)
        raise

# ЗАПУСК
if __name__ == "__main__":
    main()
