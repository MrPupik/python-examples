def add_two_numbers(num1, num2):
    return num1+num2


def say_hi():
    print('hi')


def only_y(lst):
    new_lst = []
    for name in lst:
        if name[0] == 'y':  # name.startwith('y')
            new_lst.append(name)
    return new_lst


my_names = ['yoav', 'yogev', 'idan']
new_lst = only_y(my_names)

pass
say_hi()
pass
