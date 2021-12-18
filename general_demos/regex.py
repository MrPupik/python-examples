from re import search, match, findall, MULTILINE

words = (
    "soni is the best abba, but soniarka is not\nyay my name is boo \nhow are you abba"
)
# lolipop lolipop soni abba"""


# start with soni
print(findall("^soni", words))

# ends with a
print(findall("\w*a$", words))

# contains a,o,k
print(findall("\b[a,o,k]\w*[a,o,l]\b", words))

# starts with l,s, b
print(findall("^\n*[h,s,y]\w+", words, MULTILINE))
