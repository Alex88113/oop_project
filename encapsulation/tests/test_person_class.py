import pytest

from encapsulation.person import Person


class TestPerson:
    @pytest.mark.parametrize("name, age, expected", [
        ('Alex', 19, 'Alex'),
        ('Dima', 18, "Dima"),
        ('Anton', 18, 'Anton'),
        ('Egor', 19, 'Egor')
    ])
    
    def test_name_setter(self, name, age, expected) -> None:
        person = Person(name, age)
        assert isinstance(person.name, str)
        assert person.name == expected
        assert 3 <= len(person.name) <= 15
    
    @pytest.mark.parametrize("name, age, expected", [
        ('Alex', 19, 19),
        ('Dima', 18, 18),
        ('Anton', 18, 18),
        ('Egor', 19, 19)
    ])
    
    def test_age_setter(self, name, age, expected) -> None:
        person = Person(name, age)
        assert isinstance(person.age, int)
        assert person.age == expected
        assert person.age > 0
        
    @pytest.mark.parametrize("invalid_name", [
    (""),
    ('        '),
    ('A'),
    ('kkkkdfkdnfkdnfndkfndj')
    ])
    
    def test_value_exception_name(self, invalid_name) -> None:
        with pytest.raises(ValueError):
            Person(invalid_name, 19)
            
    @pytest.mark.parametrize("invalid_name", [
        (None),
        (13232),
        (True),
        (False),
        ([])
    ])
    
    def test_type_exception_name(self, invalid_name) -> None:
        with pytest.raises(TypeError):
            Person(invalid_name, 18)
            
    @pytest.mark.parametrize("invalid_age", [
        (-1),
        (0),
        (121),
        (15),
        (150)
    ])
    
    def test_value_error_age(self, invalid_age) -> None:
        with pytest.raises(ValueError):
            Person('shura', invalid_age)
            
    @pytest.mark.parametrize("invalid_age", [
        (''),
        ('       '),
        (None),
        ('fkdmfkmdf'),
        ("26"),
        (23.32)
    ])
    
    def test_type_exception(self, invalid_age) -> None:
        with pytest.raises(TypeError):
            Person('shura', invalid_age)
