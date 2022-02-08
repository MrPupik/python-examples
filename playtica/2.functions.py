# def add_two_numbers(num1, num2):
#     return num1+num2


# a = 2


# def say_hi():
#     print(a)


# say_hi()
# print(a)


# def only_y(lst):
#     new_lst = []
#     for name in lst:
#         if name[0] == 'y':  # name.startwith('y')
#             new_lst.append(name)
#     return new_lst


# my_names = ['yoav', 'yogev', 'idan']
# new_lst = only_y(my_names)


# # q1
# def is_even(num):
#     return 0 if num % 2 == 0 else 1


# # num = input('enter number ')
# # print(is_even(num))

# # q3


# def num_of_digits(num):
#     i = 0
#     while num >= 1:
#         i += 1
#         num = num/10
#     return i


# length = num_of_digits(9999)

# # 6


# def give_discount(price):
#     prec = input("what precentage is discount?")
#     return price * prec / price


# def calc_price(price):
#     if price > 1000:
#         return give_discount(price)
#     return price * 0.9


# # scope of module
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


from pyparsing import original_text_for


def add_5(num):
    num += 5
    # print(num)


num_of_ether = 4

add_5(num_of_ether)  # num_of_ether is still 4


def lst_add_5(lst):
    for i in range(len(lst)):
        lst[i] += 5


# list_of_ether = [2, 4, 5]

# lst_add_5(list_of_ether)  # lst is now [7,9,10]

# # lst is mutable, num is not
# print(num_of_ether)
# print(list_of_ether)


# # optional paramters
# def join_strings(str1, str2='shalom'):
#     return str1 + str2


# print(join_strings('i', '+'))
# print(join_strings('i'))

# # named args
# join_strings(str2='lom', str1='sha')

# # positional args
# join_strings('sha', 'lom')


# documetation
def load_grades(file_name: str) -> dict:
    """loads all grades from `file_name` file and returns `dict` {name:grade}"""
    pass


# return
def lst_add_5(lst):
    for i in range(len(lst)):
        lst[i] += 5
        return lst  # exit here

    lst[i] = 1000  # this will never happen


print(lst_add_5([1, 2]))


# no return == return None
def mul_by_3(num):
    num = num * 3


def mul_by_3(num):
    num = num * 3
    return None

# return multiple values


def mul_by_3(num):
    result = num * 3
    return num, result


my_num = 9
original, result = mul_by_3(my_num)
print(original, result)


global_var = 1

# inner func


def outer_func():
    global global_var
    name = 'itay'
    my_var = 3

    def inner_func(name):
        nonlocal my_var  # now my_var is the same as 'my_var' my_var
        my_var = 2

        print("hello "+name)
    inner_func(name)


print(outer_func())  # hello itay
# print(inner_func())  # error ! no such thing "inner_func"


def gen_mul_by_6():

    def mul_by_6(num):
        return num*6

    return mul_by_6


my_func = gen_mul_by_6()
my_func(3)  # 18


def mul_by(multi):

    def mul(num):
        nonlocal multi
        return num*multi

    return mul


mul_by_6 = mul_by(6)
print(mul_by_6(3))
mul_by_4 = mul_by(4)

mul_by(6)(4)  # trippy as f***

