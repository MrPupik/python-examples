import json
import pickle
from io import UnsupportedOperation
file = None
try:
    file = open('example.txt', 'w')
    file.write('good mornning')
except Exception as e:
    print("handle error")
finally:
    if file:
        file.close()


# read
with open('example.txt', 'r') as file:
    content = file.read()


# cannot read if not exist
try:
    with open('another_example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("file not found")


# write is from the begining
with open('example.txt', 'w') as file:
    file.write('good afternoon')


# append is for adding
with open('example.txt', 'a') as file:
    file.write('\ngood evening')


# work with cursor
with open('example.txt', 'w') as file:
    file.write('good afternoon')
    file.flush()
    file.seek(5)
    file.write('---')


# write cannot read
try:
    with open('example.txt', 'w') as file:
        file.write('\n how are you?')
        content = file.read()
except UnsupportedOperation:
    print('cannot read !')


# write + read
with open('example.txt', 'w+') as file:
    file.write('\n how are you?')
    content = file.read()
    lines = ['hello there many times !\n' for i in range(50)]
    file.seek(0)
    file.writelines(lines)

# iterate over file
with open('example.txt', 'r+') as file:
    count = 0
    lines = []
    for row in file:
        count += 1
        lines.append(row[:-1]+' '+str(count)+'\n')
    file.seek(0)
    file.writelines(lines)


my_daya = {"mr beast": 100000, "pewdipy": 200000}

with open('my_data.bin', 'wb') as file:
    pickle.dump(my_daya, file)
    s = pickle.dumps(my_daya)

with open('my_data.bin', 'rb') as file:
    another_data = pickle.load(file)

print(another_data)

this_is_dict = {"hair": "black", "height": 180,
                "address": "ben gurion 5, kirait ata"}


this_is_json = json.dumps(this_is_dict)
this_is_dict_again = json.loads(this_is_json)

pass
