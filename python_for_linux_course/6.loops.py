# for loop
some_string = "abcdefghi"
for letter in some_string:
    print(letter)

some_list = [1, 2, 3, 4, 5]
for item in some_list:
    print(item)

for number in range(10):
    print(number)

# range(from, to, step) ---> like list[from:to:step]
range(3)  # 0,1,2
range(1, 5)  # 1,2,3,4
range(1, 6, 2)  # 1,3,5
range(5, 0, -1)  # 5,4,3,2,1

word = None

# while loop
while word != 'q':
    word = input('press q to exit')


# question 1 - avg of 10 numbers
total_sum = 0
for i in range(9):
    total_sum += int(input('enter next number '))
print(f"avg is {total_sum / 10}")

# version with validation
total_sum = 0
for i in range(10):
    next_num = input('enter next number ')

    # while the next_num is not a string of anumber - keep asking for next number
    while not next_num.isdigit():
        print("this is not a number")
        next_num = input('enter next number ')
    total_sum += int(next_num)


print(f"avg is {total_sum / 10}")


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

current_number = None
my_list = []
while current_number != 0:
    current_number = int(input('enter next number (to finish - enter 0) '))
    my_list.append(current_number)


print(f'max num is: {max(my_list)}, min num is {min(my_list)}.')


# question 2 conditions_loops file - bigger than avg
A = [1, 1, 3, 4.0, 5, 2]


avg = sum(A) / len(A)

# without sum()
num = 0
total = 0

while num < len(A):
    total += A[num]
    num += 1

for num in A:
    if num > avg:
        print(num)
