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
