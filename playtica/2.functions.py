def add_two_numbers(num1, num2):
    return num1+num2


def say_hi():
    print('hi')


say_hi()


def only_y(lst):
    new_lst = []
    for name in lst:
        if name[0] == 'y':  # name.startwith('y')
            new_lst.append(name)
    return new_lst


my_names = ['yoav', 'yogev', 'idan']
new_lst = only_y(my_names)


# q1
def is_even(num):
    return 0 if num % 2 == 0 else 1


# num = input('enter number ')
# print(is_even(num))

# q3


def num_of_digits(num):
    i = 0
    while num >= 1:
        i += 1
        num = num/10
    return i


length = num_of_digits(9999)

# 6


def give_discount(price):
    prec = input("what precentage is discount?")
    return price * prec / price


def calc_price(price):
    if price > 1000:
        return give_discount(price)
    return price * 0.9
