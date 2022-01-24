#################################################


# 1

import sys

a = int(input("enter number:"))
if a >= 0:
    print("yes")
else:
    print("no")


#################################################


# 2

a = int(input("enter number:"))
if a > 0:
    print("yes")
else:
    print("no")


#################################################


# 3

a = int(input("enter number:"))
b = int(input("enter number:"))
op = int(input("enter op:"))

if op == 1:
    print(a + b)
elif op == 2:
    print(a - b)
else:
    print("invalid operation. please enter one of: 1,2")


#################################################


# 4

first = input("enter first name:")
last = input("enter last name:")
g = input("enter gender (m/f)")

if g == "m":
    s = "Mr."
else:
    s = "Mrs."

print("Hello ", s, first, last, "Nice to meet you")

#################################################


# 5
a = int(input("enter number:"))
if a < 0:
    a *= -1
print(a)


#################################################


# 6

a = int(input("enter number:"))
if a % 2 == 0:
    print("yes")
else:
    print("no")


#################################################


# 7

a = int(input("enter number:"))
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")


#################################################


# 8

a = int(input("enter first team score:"))
b = int(input("enter second team score:"))

if a > b:
    print("first team won")
elif a < b:
    print("second team won")
else:
    print("tie")


#################################################


# 9

a = int(input("submit all ex?:"))
b = int(input("exam grade:"))
if a == 1 and b > 60:
    print("pass")
else:
    print("fail")


#################################################


# 10 - 12
# not relevant (added by error)


#################################################


# 13

a = int(input("enter number:"))
if a % 2 == 0 and a > 0:
    print("yes")
else:
    print("no")


#################################################


# 14

a = int(input("enter number:"))
if 0 <= a <= 100:
    print("yes")
else:
    print("no")


#################################################


# 15

a = int(input("enter number:"))
if 10 <= a <= 99:
    print("yes")
else:
    print("no")


#################################################


# 16
years = int(input("enter years:"))
claims = int(input("enter claims:"))
price = int(input("enter base price:"))
if years > 5 and claims < 10:
    print(price * 0.85)
else:
    print(price)


#################################################


# 17
years = int(input("enter years:"))
claims = int(input("enter claims:"))
price = int(input("enter base price:"))
if years > 5 or claims < 10:
    print(price * 0.85)
else:
    print(price)


#################################################


# 18
a = int(input("enter year:"))
if (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0)):
    print("yes")
else:
    print("no")


#################################################


# 19

a = int(input("enter edge a:"))
b = int(input("enter edge b:"))
c = int(input("enter edge c :"))
if (a < b + c) and (b < a + c) and (c < a + b):
    print("legal")
else:
    print("not legal")
