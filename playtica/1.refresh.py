number = 5
st = 'weod'
lst = [1, 2, 3]


d = {'itay': 27}
list(d.keys())[0]


# ex 22
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


# higest grade

grades = {
    90: 'itay',
    80: 'noam'
}
max_grade = max(grades.keys)  # higest grade
print(f" {grades[max_grade]} got {max_grade}")


grades = [90, 80]
names = ['itay', 'noam']

index = grades.index(max(grades))
name = names[index]
