import pytest

from encapsulation.product import Product


def _validation_title_product(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("Title a product is not string type")
    
    clear_strip_title: str = title.strip().capitalize()
    
    if not clear_strip_title:
        raise ValueError("field with title a product is empty")
    
    if not 4 <= len(clear_strip_title) <= 15:
        raise ValueError("The length of the product name should be beetwen 3 - 30 simbols")
    
    return clear_strip_title

def get_title_product(title: str) -> dict[str, str]:
    valid_title = _validation_title_product(title)
    return dict(title=valid_title)

def test_title_product() -> None:
    get_product = get_title_product("Milk")
    assert isinstance(get_product.get('title'), str)
    assert get_product.get('title') is not None
    assert get_product.get('title') == "Milk"
    
@pytest.mark.parametrize("title, expected", [
    ("   breed    ", "Breed"),
    ("MILK", "Milk"),
    (" COFFee   ", "Coffee")
])

def test_positive_scenarios(title: str, expected: str) -> None:
    get_product = get_title_product(title)
    assert get_product['title'] == expected

@pytest.mark.parametrize("invalid_title", [
    (12121),
    (None),
    (False),
    (True),
    (-2323)
])

def test_type_exceptions(invalid_title) -> None:
    with pytest.raises(TypeError):
        get_product = get_title_product(invalid_title)
        
@pytest.mark.parametrize("invalid_title", [
    (''),
    ('           '),
    ('43'),
    ('fjokdjfkdnfjkdnfjndjfn'),
    ('we')
])

def test_value_exception(invalid_title) -> None:
    with pytest.raises(ValueError):
        get_product = get_title_product(invalid_title)


class TestProduct:
    @pytest.mark.parametrize("title, expected", [
        ("Молоко", "Молоко"),
        ('Хлеб', 'Хлеб'),
        ('Мясо', 'Мясо'),
        ('Бананы', 'Бананы'),
        ('Орехи', 'Орехи')
    ])
    
    def test_title_product(self, title: str, expected: str) -> None:
        product = Product(title, 1000.)
        assert isinstance(product.title, str)
        assert type(product.title) is str
        assert product.title == expected
        
        
    @pytest.mark.parametrize("price, expected", [
        (1000.0, 1000.0),
        (5000.999, 5000.999),
        (450.0, 450.0),
        (193.23, 193.23),
        (10000000000000.000, 10000000000000.000)
    ])
    
    def test_product_price(self, price: float, expected: float) -> None:
        product = Product("Coffee", price)
        assert product.price == expected
        assert isinstance(product.price, float)
        assert type(product.price) is float
    
    @pytest.mark.parametrize("price, discount, expected", [
        (1000.0, 10, 900.0),      # 10% от 1000 = 900
        (1000.0, 0, 1000.0),      # 0% = цена без изменений
        (1000.0, 100, 0.0),       # 100% = бесплатно
        (500.0, 50, 250.0),       # 50% от 500 = 250
        (999.99, 33.3, 666.99333),   # float скидка, проверяем округление
    ])
    
    def test_discount_percent_price(self, price, discount, expected):
        product = Product("milk", price)
        assert product.get_discount_price(discount) == expected
        
        
    @pytest.mark.parametrize("invalid_title", [
        (None),
        (False),
        (121),
        (0),
        (True),
        (-43493)
    ])
    
    def test_type_exception_title(self, invalid_title) -> None:
        with pytest.raises(TypeError):
            product = Product(invalid_title, 1332.32)
            product.title = invalid_title
            
    @pytest.mark.parametrize("invalid_title", [
        (''),
        ('           '),
        ('212'),
        ('gkkfgkfmgkfmgkfmk'),
        ('d3'),
        ('A        ')
    ])
    
    def test_value_exception_title(self, invalid_title) -> None:
        with pytest.raises(ValueError):
            product = Product(invalid_title, 1332.32)
            product.title = invalid_title
            
    @pytest.mark.parametrize("invalid_price", [
        (None),
        ('gknfnfnjdnfjdn'),
        (''),
        ('          '),
        ('329389283928')
    ])
    
    def test_type_exception_price(self, invalid_price) -> None:
        with pytest.raises(TypeError):
            product = Product("Coffee", invalid_price)
            product.price = invalid_price
            
    @pytest.mark.parametrize("invalid_price", [
        (-121.0),
        (0),
        (-12121),
        (0.0),
        (-43984),
        (-23.231)
    ])
    
    def test_value_exception_price(self, invalid_price) -> None:
        with pytest.raises(ValueError):
            product = Product('breed', invalid_price)
            product.price = invalid_price
