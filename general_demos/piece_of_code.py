# calc the sallary of your employees

# cost of hour of work
hourly_pay = [100, 80, 60, 40, 80, 80, 90]

# number of hours in mounth
hours = 180

# list of employees
employee_names = ['yotam', 'yoav', 'yogev', 'yoad', 'yossi', 'yoni', 'yaniv']

num_of_employees = len(employee_names)

# print all prices
print("all hours:")
for price in hourly_pay:
    print(price)

# calculate the sallaries and print them
for i in range(0, num_of_employees):
    name = employee_names[i]
    price = hourly_pay[i]
    sallary = price*hours
    if name[0:2] == 'yo':
        sallary = sallary + 1000
    else:
        sallary = sallary - 1000

    print(f"{name}'s sallary is {sallary}")

print("\n\n second version")

# more pythonic way
for name, price in zip(employee_names, hourly_pay):
    sallary = price*hours
    if name[0:2] == 'yo':
        sallary = sallary + 1000
    else:
        sallary = sallary - 1000

    print(f"{name}'s sallary is {sallary}")

print("\n\n third version")

# extramly pythonic way
[print(f"{name}'s sallary is {price*hours + 1000 if name[:2] == 'yo' else price * hours - 1000}") for name, price in zip(
    employee_names, hourly_pay)]
