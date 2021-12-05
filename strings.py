word = "AGFVFGDGFDGF"

## first
for i in range(0,len(word), 3):
    print(word[i:i+3])

## second
for s in [word[i : i + 3] for i in range(0, len(word), 3)]:
    print(s)

## third
[print(word[i : i + 3]) for i in range(0, len(word), 3)]
    