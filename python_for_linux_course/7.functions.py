# functions - simple examples


print("start")


def add_two_number(num1, num2):
    return num1+num2


def say_hello(name):
    print('hello there ' + name)


print("def end")

num1 = 4
num2 = 100

result = add_two_number(num1, num2)
print('result is ', result)


print(say_hello('itay'))

TOTAL_HOURS = 180

# employees ecample from hello world file


def calc_salary_with_bonus(name, hour_sallary):
    if name.startswith("yo"):
        result = TOTAL_HOURS * hour_sallary + 1000
    else:
        result = TOTAL_HOURS * hour_sallary - 1000

    return result


def calc_salary_with_bonus2(name, hour_sallary):
    if name.startswith("yo"):
        return TOTAL_HOURS * hour_sallary + 1000
    return TOTAL_HOURS * hour_sallary - 1000


employees = {"yotam": 100, "yoav": 80, "yogev": 90, "yoad": 120, "yaniv": 90}

salaries = {}


for name, hour_sallary in employees.items():
    salaries[name] = calc_salary_with_bonus(name, hour_sallary)

print(salaries)
