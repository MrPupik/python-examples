class Car:
    NUMBER_OF_WHEELS = 4
    FUEL_PER_KM = 0.05
    SEATS = 4


    def __init__(self, fuel: float, kilometraj=0) -> None:
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


class Taxi(Car):
    KM_COST = 2

    def __init__(self, fuel: float, money=0, kilometraj=0) -> None:
        self.__money = money
        super().__init__(fuel, kilometraj=kilometraj)

    @property
    def money(self):
        return self.__money * 0.9

    @money.setter
    def money(self, coins):
        self.__money += coins

    def drive(self, km):
        l = super().drive(km)
        price = l * self.KM_COST
        self.__money += price
        if l == km:
            print(f"Thanks, it was {km * self.KM_COST} shekels. good day !")
        elif l > 0:

            print(
                f"Terribly sorry, but We drove only {l} km,
                 i charged you {km * self.KM_COST}. good day !"
            )
        else:
            print("sorry, i can't take you today.")
        return price


class Lemo(Taxi):
    KM_COST = 10
    SEATS = 100

    def beep(self):
        print("*********************")
        print("*********************\n***** DING DONG *****\n*********************")
        print("*********************")


class Van(Taxi):
    KM_COST = 6
    SEATS = 12


class Minibus(Taxi):
    KM_COST = 8
    SEATS = 25
