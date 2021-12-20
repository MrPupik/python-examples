from general_demos.classes import Person


class Student(Person):
    def __init__(self, name: str, id: int | str, age: int, grades: dict, school) -> None:
        self.school = school
        self.grades = grades
        super().__init__(name, id, age)

    def get_avg(self):
        return sum(self.grades.values()) / len(self.grades)

    def add_grade(prof, grade):
        self.grades[prof] = grade

    def __getitem__(self, item):
        return self.grades[item]

    def __setitem__(self, item, value):
        self.grades[item] = value

    def __iter__(self):
        return ((prof, grade) for prof, grade in self.grades.items())


s = Student("miri", 0, 33, {"math": 90, "python": 80}, "TAU")
for prof, grade in s:
    print(f"{prof}: {grade}")
