# # solutions

# # 1
# print("6+2=", 6+2)
# print("6-2=", 6-2)
# print("6*2=", 6*2)

# #####################################

# # 2
# print("6/2=", 6/2)
# print("6//2=", 6//2)
# print("6%2=", 6 % 2)

# #####################################
# # 3
# print("5+2=", 5+2)
# print("5-2=", 5-2)
# print("5*2=", 5*2)
# print("5/2=", 5/2)
# print("5//2=", 5//2)
# print("5%2=", 5 % 2)

# #####################################

# # 4
# a = int(input("enter num:"))
# b = int(input("enter num:"))

# c = a+b
# d = a-b
# e = a*b
# f = a/b

# print(a, b, c, d, e, f)

# #####################################

# # 5
# a = int(input("enter num:"))
# b = int(input("enter num:"))

# c = a+b
# d = a-b
# e = a*b
# f = a/b

# print("a  |  b	| c=a+b | d=a-b | e=a*b | f=a/b")
# print("{0:3d}{1:4d}{2:7d}{3:7d}{4:7d}{5:10.2f}".format(a, b, c, d, e, f))

# #####################################

# # 6

# a = int(input("enter num:"))
# b = int(input("enter num:"))

# c = a+b
# print(c)

# c = a-b
# print(c)

# c = a*b
# print(c)

# c = a/b
# print(c)


# #####################################

# # 7
# a = int(input("enter num:"))
# b = int(input("enter num:"))
# c = int(input("enter num:"))

# print(a+b+c)

# #####################################

# # 8
# s = 0
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# print(s)


# #####################################

# # 9

# s = 0
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# print(s)


# # 9

# s = 0
# for i in range(5):
#     a = int(input("enter num:"))
#     s += a

# print(s)


# #####################################

# # 10

# a = int(input("enter num:"))
# b = int(input("enter num:"))
# c = int(input("enter num:"))
# d = int(input("enter num:"))
# e = int(input("enter num:"))

# print((a+b-c)*d/e)

# #####################################

# # 11

# s = 0
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s -= a
# a = int(input("enter num:"))
# s *= a
# a = int(input("enter num:"))
# s /= a

# print(s)

# #####################################

# # 12

# a = int(input("enter num:"))
# print(a**2)


# #####################################

# # 13
# a = int(input("Enter a number:"))
# print("The square of", a, "is:", a**2)


# #####################################

# # 14
# a = int(input("enter num:"))
# b = int(input("enter num:"))
# c = int(input("enter num:"))
# print("X  |  X*X")
# print("{0:3d}{1:4d}".format(a, a**2))
# print("{0:3d}{1:4d}".format(b, b**2))
# print("{0:3d}{1:4d}".format(c, c**2))


# #####################################

# # 15
# a = int(input("enter num:"))
# b = int(input("enter num:"))
# print(a*b/2)

# #####################################

# # 16
# a = int(input("enter num:"))

# print(a*0.17)


# #####################################

# # 17

# a = int(input("enter num:"))

# print(a*1.17)


# #####################################

# # 18 + 19
# a = int(input("enter num:"))

# print(a/1.17, (a/1.17)*0.17)


# #####################################

# # 20
# s = 0
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# a = int(input("enter num:"))
# s += a
# print(s/5)


# #####################################

# # 21
# name = input("enter name:")
# sal = int(input("enter the monthly pay:"))
# additions = int(input("enter the sum of additions:"))

# print(name, "salary is", sal*0.9 + additions)


# #####################################

# # 22
# b = int(input("enter ammount of blue:"))
# r = int(input("enter ammount of red:"))
# g = int(input("enter ammount of green:"))
# y = int(input("enter ammount of yellow:"))

# print(r*75 + y*80 + g*100 + b*120)


# 22 with dict
fabric_prices = {
    "red": 75,
    "yellow": 80,
    "green": 100,
    "blue": 120
}
total_price = 0
for color, price in fabric_prices.items():
    amount = int(input(f"enter amount of {color} fabric: "))
    total_price += amount*price  # key * dict[key]
print('total price is', total_price)


print('total price is', sum(
    [price * int(input(f"enter amount of {color} fabric: ")) for color, price in fabric_prices.items()]))

#####################################

# 23

print("This progeam solves a system of two linear equations")
print("Enter the coefficients of the first equation (a1, b1, c1)")
a1 = int(input(""))
b1 = int(input(""))
c1 = int(input(""))
print("Enter the coefficients of the second equation (a1, b1, c1)")
a2 = int(input(""))
b2 = int(input(""))
c2 = int(input(""))

x = ((c1*b2) - (c2*b1))/((a1*b2) - (a2*b1))
y = ((a1*c2) - (a2*c1))/((a1*b2) - (a2*b1))

print("The solution is:x=", x, "y=", y)
