class MyList:
    def __init__(self, data: list) -> None:
        self.data = data
        self.max = len(data)

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.max:
            rslt = self.data[self.i]
            self.i += 1
            return rslt
        raise StopIteration()


l = MyList(list(range(9)))
l[1] = 3
print(l[1])
print("good")

for i in l:
    print(i)


def simple_generator():
    i = 0
    while i < 100:
        a = yield i
        if a:
            i = a
        else:
            i += 1


sg = simple_generator()


# example - DrugManager
class DrugManager:
    def __init__(self, schedual: dict) -> None:
        self.schedual = schedual
        self.days = (
            "sunday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
        )

    def add_drug(self, day, drug_name):
        self.schedual[day] = drug_name

    def __getitem__(self, day):
        return self.schedual[day]

    def __setitem__(self, day, drug):
        self.schedual[day] = drug

    def __iter__(self):
        self.day = -1
        return self

    def __next__(self):
        self.day += 1
        if self.day >= len(self.days):
            raise StopIteration
        return self.schedual.get(self.days[self.day], "no drug today")


d = DrugManager({"sunday": "a", "tuesday": "b", "friday": "c"})

d = iter(d)
for n in d:
    print(n)


d["monday"] = "z"

for n in d:
    print(n)
