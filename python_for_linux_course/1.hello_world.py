# cost of hour of work
hourly_pay = [100, 80, 60, 40, 80, 80, 90]

# hours in month
hours = 180

# list of my employees
employee_names = ['yotam', 'yoav', 'yogev', 'yoad', 'yossi', 'yoni', 'yaniv']

print("all hours:")
for price in hourly_pay:
    print(price)

num_of_employees = len(employee_names)
bunous = 1000
print("\nall sallaries:")


# calcute the sallaries of all
for name, price in zip(employee_names, hourly_pay):
    sallary = price*hours

    if name[0:2] == 'yo':
        sallary = sallary + bunous
    else:
        sallary = sallary - bunous

    print("sallary of", name, "is:", sallary)


[print(f"{name}'s sallary is {price*hours + 1000 if name[:2] == 'yo' else price * hours - 1000}") for name, price in zip(
    employee_names, hourly_pay)]
