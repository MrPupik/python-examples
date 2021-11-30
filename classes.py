__doc__ = "this is the classes module. here we show OOP stuff"


class Car:
    NUMBER_OF_WHEELS = 4
    FUEL_PER_KM = 0.05

    def __init__(self, fuel: float, kilometraj: int) -> None:
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
            length = int(self.fuel / Car.FUEL_PER_KM)
            self.fuel = 0
        else:
            length = km
        self.distance += length
        return length

    def refuel(self, fuel: int):
        """
        refuels

        return current fuel
        """
        self.fuel += fuel
        return self.fuel


b = Car(10, 0)


class AmericanGrade(int):
    Grades = {100: "A", 90: "B", 80: "C", 70: "D", 60: "F"}

    def __new__(cls, grade):
        val = None
        for numeric_grade in AmericanGrade.Grades.keys():
            if AmericanGrade.Grades[numeric_grade] == grade:
                val = numeric_grade
        if not val:
            raise ValueError("Invalid American grade")
        return super().__new__(cls, val)

    def __init__(self, g) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return AmericanGrade.Grades[self]


b = AmericanGrade("F")
