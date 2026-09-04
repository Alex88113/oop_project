from loguru import logger

logger.add(
    'logs/bank_log.log',
    level='DEBUG'
)

class BankAccount:
    def __init__(self, account_number: str, balance: float=0.0) -> None:
        self.account_number = account_number
        self.balance = balance
        self._transaction_history: list[str] = []

    @staticmethod
    def _validation_amount_sum(amount: float | int) -> float | int:
        if not isinstance(amount, (float, int)):
            raise ValueError("Некорректный тип суммы")

        if not amount:
            raise ValueError("Сумма не указана")

        if amount < 0:
            raise ValueError("Сумма отрицательна")

        return amount

    def deposit(self, amount: float | int) -> float:
        valid_amount = self._validation_amount_sum(amount)
        self.balance += valid_amount
        self._transaction_history.append(f'Счет пополнен на: {amount}$')
        return float(self.balance)

    def withdrawal(self, amount: float | int) -> None:
        valid_amount = self._validation_amount_sum(amount)
        if not valid_amount > self.balance:
            self.balance -= amount
            self._transaction_history.append(f'С баланса снято: {amount}$')
        else:
            raise ValueError("Сумма снятия превышает текущую сумму на балансе")

    def show_transaction_history(self):
        if not self._transaction_history:
            logger.warning("История транзакций пуста")
            return None

        logger.debug('------------ Transaction History ------------')
        for index, line in enumerate(self._transaction_history):
            logger.debug(f"{index}: {line}")
        logger.debug("-" * 45)
        return None


account = BankAccount('3434 434 4343 34322', 10.000)
account.deposit(1212)
account.deposit(9000)
account.deposit(58909)

account.withdrawal(1000)
account.withdrawal(500)
account.withdrawal(192)
account.show_transaction_history()