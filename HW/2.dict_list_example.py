NUM_OF_STUDENTS = 5

# getting the data: name and grade from 5 students
print("hello there")
all_grades = {}

for n in range(NUM_OF_STUDENTS):
    name = input(f"please enter name {n+1}\n")
    grade = int(input(f"please enter grade {n+1}\n"))
    all_grades[name] = grade

# getting the minimal letter
min_letter = min(all_grades.keys())[0]

current_max_grade = -1
current_max_name = ""
# getting max grade
for k in [k for k in all_grades if k[0] == min_letter]:
    if all_grades[k] > current_max_grade:
        current_max_grade = all_grades[k]
        current_max_name = k

print(
    f"the minimum letter is '{min_letter}'"
    + f"\nthe maximus grade is the grade of {current_max_name}, who got {current_max_grade}"
)


# show off
all_grades = {
    input(f"please enter name {n+1}\n"): int(input(f"please enter grade {n+1}\n"))
    for n in range(NUM_OF_STUDENTS)
}
max_grade = max([i[1] for i in all_grades.items()
                if i[0][0] == min(all_grades)[0]])
print("max grade is ", max_grade)
