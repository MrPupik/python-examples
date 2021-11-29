__doc__ = "this is the classes module. here we test OOP stuff"

class poop:
    def __init__(self) -> None:
        self.p = "hooo"

    @classmethod
    def peep(self):
        pass

    @staticmethod
    def poopi():
        print("static")

    def st():
        pass

    @staticmethod
    def ft(self):
        pass


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
        print("happen")
        super().__init__()

    def __repr__(self) -> str:
        return AmericanGrade.Grades[self]


b = AmericanGrade("F")
