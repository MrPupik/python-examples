from TaxiStation.utils import get_type_name


class Car:
    NUMBER_OF_WHEELS = 4
    FUEL_PER_KM = 0.05
    SEATS = 4

    def __init__(self, fuel: float, kilometraj=0) -> None:
        self.available = True
        self.fuel = fuel
        self.distance = kilometraj

    def beep(self):
        print("*********************\n***** BEEEEEEEP *****\n*********************")

    def drive(self, km: int):
        """### drive `km` kilometers.
        if not enough fuel - driving until no more fuel

        returns distance travled"""
        fuel_needed = km * 0.05
        if fuel_needed > self.fuel:
            length = int(self.fuel / self.FUEL_PER_KM)
            self.fuel = 0
        else:
            length = km
            self.fuel -= fuel_needed
        self.distance += length
        return length

    def refuel(self, fuel: int):
        """
        refuels

        return current fuel
        """
        self.fuel += fuel
        return self.fuel

    @staticmethod  # without this i could car1.set_fuel_per_km()
    def set_fuel_per_km(new_value):
        Car.FUEL_PER_KM = new_value

    def __repr__(self) -> str:
        return f"{get_type_name(self)}: {self.fuel} fuel, {self.distance} kilometraj"
