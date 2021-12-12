################# question 1
str1 = str(str1)
start_eq_end = str1[:3] == str1[-1:-4:-1]
if len(str1) > 5 and start_eq_end and str1[6].lower() == "d":
    print("Yes")
else:
    print("No")


################# question 2

A = [8, 9, 9, 9, 9, 10, 12, 10, 10]


## while loop:
sum = 0
num_above_avg = 0

# sum up all elements
while count < len(A):
    sum += A[count]
    count += 1

# get the avarege
avg = sum / count
count = 0

# count how many are bigger than avg
while count < len(A):
    if A[count] > avg:
        num_above_avg += 1
    count += 1
print("The number of elements bigger than the average is: " + str(num_above_avg))


## for loop
num_above_avg = 0
sum = 0
count = 0

for num in A:
    sum += num
avg = sum / len(A)

for num in A:
    if num > avg:
        num_above_avg += 1
print("The number of elements bigger than the average is: " + str(num_above_avg))
