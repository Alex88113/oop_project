from classes_and_object.utils.logger import logger


class BankAccount:
    def __init__(self, account_number: str, balance: float = 0.0) -> None:
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return float(self._balance)

    @account_number.setter
    def account_number(self, value: str) -> None:
        if not isinstance(value, str):
            logger.error(f"Номер счета должен быть строкой а не: {value}")
            raise TypeError(f"Номер счета должен быть строкой а не: {value}")

        clear_account_number: str = value.strip()

        if not clear_account_number:
            logger.error("поле с номером карты пустое")
            raise ValueError("поле с номером карты пустое")

        if not 10 <= len(clear_account_number) <= 30:
            logger.error("Недостаточная длина номера вашего счета.")
            raise ValueError("Недостаточная длина номера вашего счета.")

        self._account_number = value

    @balance.setter
    def balance(self, value: float | int) -> None:
        if not isinstance(value, (float, int)):
            logger.error("Неподходящий тип суммы баланса")
            raise TypeError("Неподходящий тип суммы баланса")

        if value < 0:
            logger.error("Баланс не может быть отрицательным")
            raise ValueError("Баланс не может быть отрицательным")

        self._balance = float(value)


class BankService(BankAccount):
    def __init__(self, account_number: str, balance: float) -> None:
        super().__init__(account_number, balance)
        self._transaction_history: list[str] = []
        self._count_operations: int = 0

    @staticmethod
    def _validation_amount_sum(amount: float | int) -> float | int:
        if not isinstance(amount, (float, int)):
            logger.error("сумма не явялется числом")
            raise TypeError("сумма не явялется числом")

        if amount < 0:
            logger.error("Указанная сумма отрицательная")
            raise ValueError("Указанная сумма отрицательная")

        return amount

    def deposit(self, amount: float | int) -> float:
        get_valid_amount = self._validation_amount_sum(amount)
        self._balance += get_valid_amount
        self._count_operations += 1
        self._transaction_history.append(f"Баланс пополнен на: {get_valid_amount}$")
        return self._balance
    
    def withdrawal(self, amount: float) -> None:
        valid_amount = self._validation_amount_sum(amount)
        if valid_amount <= self._balance:
            self._balance -= valid_amount
            self._count_operations += 1
            self._transaction_history.append(f"Снято средств: {valid_amount}")
            return
        else:
            logger.warning("Сумма снятия превышает сумму денег на балансе")
            raise ValueError("Сумма снятия превышает сумму денег на балансе")

    def print_transaction_history(self) -> None:
        if not self._transaction_history:
            logger.warning("список с операциями пуст")
            raise ValueError("список с операциями пуст")

        logger.info("-" * 70)
        for index, history in enumerate(self._transaction_history):
            logger.info(f"{index}. {history}")
        logger.debug(f"Количество совершенных банковских операций = {self._count_operations}")
        logger.info("-" * 70)


def main() -> None:
    try:
        bank_service = BankService("2323 323 3232", 323.32)
        bank_service.deposit(8989)
        bank_service.deposit(1000)
        bank_service.deposit(1000)

        bank_service.withdrawal(500)
        bank_service.withdrawal(500)
        bank_service.deposit(1000)

        bank_service.print_transaction_history()
        logger.info(f"Текущий баланс: {bank_service.balance}$")
    except TypeError as error:
        logger.error(f"переданны аргументы неподходящго типа данных: {error}")
        raise TypeError(f"переданны аргументы неподходящго типа данных: {error}")
    except Exception as error:
        logger.error(f"Возникла неизвестная ошибка: {error}")
        raise Exception(f"Возникла неизвестная ошибка: {error}")


if __name__ == "__main__":
    main()
