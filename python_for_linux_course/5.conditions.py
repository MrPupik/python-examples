# last time:
# numbers
from py import code


num1 = 5
num2 = 2.5
num3 = num1 + num2 - 3*num1

# strings
# convertion
num4 = int("5")
str_of_num = str(124)

# operators on strings
str1 = "my name is"
str2 = str1 + " itay"  # my name is itay

# get string from the user
# from_user = input('please enter the data')

# functions of str
str1.upper()
str1.endswith('itay')  # will return true

# split
lst = 'yoav | yotam | taniv'.split('|')  # [yoav, yotam, taniv]
# same as:
long_str = 'yoav | yotam | taniv'
lst = long_str.split('|')
"/usr/opt/folder/file"  # we can find the folder that file is in, using split by '/'


# list
my_list = ['1', True, 'my apple', 888]

# slicing
my_list[2:5]
my_list[2:5:2]
my_list[6:2:-1]
copy_of_list = my_list[:]
my_list[:2]
my_list[6:]
my_list[-1]


# add to list
my_list.append(55)
last_one = my_list.pop()  # remove last one
first_one = my_list.pop(0)


# new ---- conditions
# if condition:
#     - code -
# elif another_condition:
#     - code -
# else:
#     - code -

age_of_child = 8
name = None
# age_of_child = input("enter the age ")

# middle-school? high-school? elementry?
if age_of_child > 15 and age_of_child < 19:
    print("high school")
elif (age_of_child > 10 or name == "issaschar"):
    print("middle schoole")
elif age_of_child > 5:
    print("elementry schoole")
else:
    print("invalid age")


# print("hi there !")
# first_name = input("enter your first name: \n")
# last_name = input("enter your last name:  \n")
# we could also:
# [first, last ] = full_name.split(' ')
# gender = input('enter your gender: \n')

# title = None

# if gender == 'm' or gender == 'male':
#     title = 'Mr.'
# elif gender == 'f' or gender == 'female':
#     title = 'Ms.'
# else:
#     print("invalid gender")

# if title:
#     output = f"Hello, {title} {first_name} {last_name}, Nice To Meet You."
#     print(output)

var = 'some value'
if var:
    print("any valus - true")
var = None

if not var:
    print("none is not true")


# and or
