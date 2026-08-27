from typing import Annotated

from .utils.logger import logger


class BankAccount:
    """Банковский класс для совершения банковских операций"""
    def __init__(self, account_number: str, balance: float=0.0) -> None:
        self.account_number = account_number
        self._balance = balance
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, value: float) -> None:
        if not isinstance(value, int):
            logger.error("value not valid")
            raise
        
        if value <= 0:
            logger.error("Сумма пополнения отрицательна либо равна 0")
            raise
        
        self._balance = value
        
    
    def deposit(self, amount: float) -> float:
        if not isinstance(amount, float | int):
            logger.error("Тип суммы некорректен")
            raise
        
        if amount <= 0:
            logger.error("Сумма пополнения отрицательна либо равна 0")
            raise
        
        self._balance += amount
        logger.info("Баланс пополнен на: {:.2f} руб.", self._balance)
        return self._balance
    
def main() -> None:
    bank_account: BankAccount = BankAccount('343434 32323 32323 32312', 343.34)
    bank_account.deposit(23.323)
    print(f"Текущий баланс: {bank_account.balance}")
    
# ЗАПУСК
if __name__ == "__main__":
    main()
