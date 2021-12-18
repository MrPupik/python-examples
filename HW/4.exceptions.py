from general_demos.classes import Person


class UnderAgedException(Exception):
    pass


class bar:
    def __init__(self, min_age) -> None:
        self.min_age = min_age

    def enter(self, person: Person):
        if person._age <= self.min_age:
            raise UnderAgedException("this person is only "+person._age)
        return "welcom :)"
