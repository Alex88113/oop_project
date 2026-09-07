from classes_and_object.utils.logger import logger


class Product:
    def __init__(self, title: str, price: float) -> None:
        self._title = title
        self._price = price
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def price(self) -> float:
        return float(self._price)
    
    @title.setter
    def title(self, title: str) -> None:
        if not isinstance(title, str):
            logger.error("Название товара необходимо указать в виде строки")
            raise TypeError("Название товара необходимо указать в виде строки")
        
        clear_strip_title = title.strip()
        
        if not clear_strip_title:
            logger.error("Поле с названием товара пустое")
            raise ValueError("Поле с названием товара пустое")
        
        if not 4 <= len(clear_strip_title) <= 15:
            logger.error("Название товара вне диапазона от 4 - 15 символов.")
            raise ValueError("Название товара вне диапазона от 4 - 15 символов.")
        
        self._title = clear_strip_title.capitalize()
    
    @price.setter
    def price(self, price: float | int) -> None:
        if not isinstance(price, (float, int)):
            logger.error("Сумма товара должна быть числового типа")
            raise TypeError("Сумма товара должна быть числового типа")
        
        if price <= 0:
            logger.error("Сумма товара отрицательна либо равна 0")
            raise ValueError("Сумма товара отрицательна либо равна 0")
        
        self._price = price
        
    @staticmethod
    def _validation_discount_percent(discount_percent: float | int) -> float:
        if not isinstance(discount_percent, (float, int)):
            logger.error("Значение скидки необходимо указать в виде числа")
            raise TypeError("Значение скидки необходимо указать в виде числа")
            
        if not 0 <= discount_percent <= 100.0: 
            logger.error("Процент скидки не находиться в диапазоне от 0 до 100")
            raise ValueError("Процент скидки не находиться в диапазоне от 0 до 100%")
        
        return float(discount_percent)
    
    def _apply_discount_to_price(self, discount_percent: float | int) -> float:
        get_valid_discount_percent = self._validation_discount_percent(discount_percent)
        return self._price * (1 - get_valid_discount_percent  / 100)
    
    def get_discount_price(self, discount_percent: float) -> float:
        return self._apply_discount_to_price(discount_percent)
    
    def __str__(self) -> str:
        return f"Title: {self._title} | price={self._price}"
    
    def __repr__(self) -> str:
        return f"Product(title={self._title}, price={self._price})"

def main() -> None:
    try:
        product = Product("", 1000.0)
        product.price = 1500
        product.title = 'Buter'
        logger.info(f'Итоговая цена товара с учетом скидки: {product.get_discount_price(10.0)} руб.')
        logger.info(f"Демонстрация товара {str(product)}")
        logger.debug(f"Данные об объекте для разработчиков: {repr(product)}")
    except TypeError as error:
        logger.error(f"Переданны значения неверного типа в параметры: {error}, type={type(error)}")
        raise
    except ValueError as error:
        logger.error(f"Некорретно переданные аргументы: {error}, type={type(error)}")
        raise
    except Exception as error:
        logger.error(f"Возникла непредвиденная ошибка в ходе выполнения программы: {error}")
        raise
    
if __name__ == "__main__":
    main()
