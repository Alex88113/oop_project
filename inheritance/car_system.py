class Vehicle:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, year, battery_capacity: int | None=0) -> None:
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def charge(self) -> None:
        print(f'chaining {self.brand} {self.model} with {self.battery_capacity} kwh battery')

electric_vehicle = ElectricVehicle("BMW", "X15", 2000)
electric_vehicle.charge()