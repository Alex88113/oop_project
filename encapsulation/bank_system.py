from abc import ABC, abstractmethod

from classes_and_object.utils.logger import logger


class BankAccount(ABC):
    def __init__(self, account_number: str, balance: float=0.0) -> None:
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float) -> float:
        pass

    @abstractmethod
    def withdrawal(self, amount: float) -> None:
        pass

    @abstractmethod
    def transaction(self, account_number: str, amount: float):
        pass

    @abstractmethod
    def show_transaction_history(self) -> None:
        pass

    def __repr__(self) -> str:
        return f"BankAccount(account_number={self._account_number}, balance={self._balance})"

    def __str__(self) -> str:
        return f"Account number: {self._account_number} | money on the balance: {self._balance}$"

class BankService(BankAccount):
    def __init__(self, account_number: str, balance: float=0.0) -> None:
        super().__init__(account_number, balance)
        self._transaction_history: list[str] = []

    @property
    def balance(self) -> float:
        return float(self._balance)

    @staticmethod
    def _validation_amount_sum(amount: float | int) -> float:
        if not isinstance(amount, (float, int)):
            logger.error("Укажите в качестве суммы любое произвольное число")
            raise TypeError("Укажите в качестве суммы любое произвольное число")

        if amount is None:
            logger.error("Поле с суммой пусто")
            raise ValueError("Поле с суммой пусто")

        if amount <= 0:
            logger.error("Сумма снятия отрицательна либо равна 0")
            raise ValueError("указанная cумма отрицательна либо равна 0")

        return amount

    def deposit(self, amount: float) -> float:
        valid_amount = self._validation_amount_sum(amount)
        self._balance += valid_amount
        self._transaction_history.append(f'Баланс пополнен на: {valid_amount}$')
        return self._balance

    def withdrawal(self, amount: float) -> None:
        valid_withdrawal_amount = self._validation_amount_sum(amount)
        if valid_withdrawal_amount <= self._balance:
            self._balance -= valid_withdrawal_amount
            self._transaction_history.append(f'Со счет снято: {valid_withdrawal_amount}$')
            return
        else:
            logger.warning("На счету недостаточно средств")
            raise ValueError("На счету недостаточно средств")

    def transaction(self, amount: float, other_number: 'BankService'):
        valid_amount = self._validation_amount_sum(amount)
        if valid_amount <= self._balance:
            self.withdrawal(valid_amount)
            other_number.deposit(valid_amount)
            self._transaction_history.append(
                f"Перевод: {valid_amount}$, получатель: {other_number._account_number}"
            )
        else:
            logger.warning("на балансе недостаточно средств для совершения перевода")
            raise ValueError("на балансе недостаточно средств для совершения перевода")

    def show_transaction_history(self) -> None:
        if not self._transaction_history:
            logger.warning('Банковских операций не было совершенно')
            return

        logger.debug('----------------- Bank Transactions -----------------')
        for index, transaction in enumerate(self._transaction_history):
            logger.debug(f"{index}: {transaction}")
        logger.debug("Текущий баланс составляет: {}$", self.balance)
        logger.debug('-' * 60)

        return

def main() -> None:
    try:
        account = BankService('12323 434 4343 232', 1000.000)
        account2 = BankService('2323 65645 4343 3232', 90000)

        # пополнение баланса
        account.deposit(6700)

        # Снятие средств
        account.withdrawal(100)

        # Переводы
        account.transaction(500, account2)

        # Выводим всю информацию об совершенных банковских операциях
        account.show_transaction_history()

    except ValueError as error:
        logger.error("Переданы аргументы некорректного типа: {}", error)
        raise

    except TypeError as error:
        logger.error("Ошибка типа данных: {}", error)
        raise

    except Exception as error:
        logger.error("Возникла неизвестная ошибка в процессе выполнения программы: {}", error)
        raise

if __name__ == "__main__":
    main()
