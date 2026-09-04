class Animal:
    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self) -> str:
        return "Gav gav.....GAV!!"


dog = Dog('max', 'Овчарка', 'yes')
print(dog.bark())