from cgitb import text


print('----- read - 1 -----')
with open('text1.txt', 'r') as f:
    print(f.read())
print('----- read - 2 -----')
with open('text1.txt', 'r') as f:
    content = f.read()
    print(content[:10])
print('----- read - 3 -----')
with open('text1.txt', 'r') as f:
    i = 1
    lines = f.readlines()
    for line in lines[:2]:
        print(line)

print('----- read - 4 -----')
with open('text1.txt', 'r') as f:
    i = 1
    for line in f:
        if i % 2 == 0:
            print(line[:-1])
        i += 1


text2 = ("Your are the worst captain I've ever seen\nBut I am a captain !\n" +
         "This is the day you will always remember\n" +
         " as the day you almost caught Captain Jack Sparrow\nYo, Ho haul together, hoist the colours high\n" +
         "Heave ho, thieves and beggars, never say we die")

####### wirte 1 ########
# with open('text2.txt', 'w') as f:
#     f.write(text2)


####### wirte 2 ########
# with open('text2.txt', 'w') as f:
#     f.write(text2[:20])


####### wirte 3 ########
# word_list = ["Bird", "boy", "clause", "Philips", "agnostic", "boring"]
# with open('text2.txt', 'w') as f:
#     for word in word_list[:-1]:
#         f.write(word+'\n')
#     f.write(word)

####### wirte 4 ########
# with open('text2.txt', 'w') as f:
#     lines = text2.split('\n')
#     for line in lines[:2]:
#         f.write(line+'\n')


####### wirte 5 ########
# with open('text2.txt', 'w') as f:
#     lines = text2.split('\n')
#     for i, line in enumerate(lines):
#         f.write(f"{i+1} {line}\n")


####### append 1 ########
# with open('text1.txt', 'a') as f:
#     f.write(text2)

####### append 2 ########
# with open('text1.txt', 'a') as f:
#     f.write(text2.split('\n')[0])

####### cursor 1 ########
with open('text2.txt', 'r+') as f:
    lines = f.readlines()
    
    f.seek(0)
    f.writelines([f'{i} {line}\n' for i, line in enumerate(lines)])
