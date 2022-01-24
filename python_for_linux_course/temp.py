# question 3 - min and max numbers given
current_number = None
max_num = -100000
min_num = 100000
while current_number != 0:
    current_number = int(input('enter next number (to finish - enter 0) '))
    if current_number > max_num:
        max_num = current_number
    if current_number < min_num:
        min_num = current_number

print(f'max num is: {max_num}, min num is {min_num}.')
