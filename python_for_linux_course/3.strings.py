2

s = input("please enter a string")

print('uppercase: ', s.upper())
print('lowercase: ', s.lower())
print('first and last: ', s[0], s[-1])
print('first 3 * 3: ', s[0:3]*3)


3
s = input("please enter a string")
start = int(input("please enter start position"))
end = int(input("please enter end position"))
print('result:', s[start:end])

# 4
s = input("please enter a string")
start = int(input("please enter start position"))
end = int(input("please enter end position"))
print('result:', s[end:start:-1])
