
# # grades in class
# d = {
#     'yuval': 88,
#     'itamar': 72
# }

# l = [88, 72]
# l[1]  # 72
# d['itamar']  # 72


# hosts = {'production': "129.164.1.4",
#          'test': "192.168.1.1",
#          }

# user_authrized = {'yoav': False,
#                   'yogev': True,
#                   }

# # employees ecample from hello world file
# employees = {'yotam': 100,
#              'yoav': 80,
#              'yogev': 90,
#              'yoad': 120,
#              'yaniv': 90}


# salaries = {}

# for key in employees:
#     salaries[key] = 180*employees[key]

# print(list(salaries.keys()))
# print(list(salaries.values()))
# print(list(salaries.items()))


# for key, value in salaries.items():
#     print(f'give the employee {key} - {value} shekels')

# # tuples - cheap lists
# tple = (1, 2, "a")
# tple[1]  # 2
# tple[0] = 8  # error - cant change tuple

# for item in tple:
#     print(item)

# # set - unique collection
# st = {1, 2, 3}
# st.add(2)  # {1,2,3}
# st2 = {3, 4, 5}
# st & st2  # {3}
# st | st2  # {1,2,3,4,5}


# question 22 first ex file

fabric_prices = {
    'red': 75,
    'yellow': 80,
    'green': 100,
    'blue': 120
}
total_price = 0
for color, price in fabric_prices.items():
    amount = int(input(f"enter amount of {color} fabric: "))
    total_price += amount * price

print(f"total price is {total_price}")
