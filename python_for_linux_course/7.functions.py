# # functions - simple examples


# print("start")


# def add_two_number(num1, num2):
#     return num1+num2


# def say_hello(name):
#     print('hello there ' + name)

# scope of module
# var = 1
# var2 = 3
# var3 = 2


# def some_func():
#     global var3
#     # scope of function
#     var = 5
#     var3 = 4
#     print(var)  # var of functions - 5
#     print(var2)  # global var2 - 3


# some_func()
# print(var3)  # is 4 now
# print(var)  # is still 1


# print("def end")

# num1 = 4
# num2 = 100

# result = add_two_number(num1, num2)
# print('result is ', result)


# print(say_hello('itay'))

# TOTAL_HOURS = 180

# # employees ecample from hello world file


# def calc_salary_with_bonus(name, hour_sallary):
#     if name.startswith("yo"):
#         result = TOTAL_HOURS * hour_sallary + 1000
#     else:
#         result = TOTAL_HOURS * hour_sallary - 1000

#     return result


# def calc_salary_with_bonus2(name, hour_sallary):
#     if name.startswith("yo"):
#         return TOTAL_HOURS * hour_sallary + 1000
#     return TOTAL_HOURS * hour_sallary - 1000


# employees = {"yotam": 100, "yoav": 80, "yogev": 90, "yoad": 120, "yaniv": 90}

# salaries = {}


# for name, hour_sallary in employees.items():
#     salaries[name] = calc_salary_with_bonus(name, hour_sallary)

# print(salaries)


# functions basic questions

def get_numbers():
    lst = []
    stop_str = 'finish'
    input_value = input('please enter next number, to finish enter "finish": ')
    while(input_value != 'finish'):
        if input_value.isdigit():
            next_num = int(input_value)
            lst.append(next_num)
        else:
            print('this is not a number')
        input_value = input(
            'please enter next number, to finish enter "finish": ')
    return lst


def get_avg(lst):
    return sum(lst) / len(lst)


def print_avg_from_numbers():
    lst = get_numbers()
    avg = get_avg(lst)
    print('avg of all numbers:', avg)


def count_digits(num):
    count = 0
    while (num >= 1):
        count += 1
        num /= 10
    print(count)
