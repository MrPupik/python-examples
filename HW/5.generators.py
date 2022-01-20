# 1
def generators_list():
    i = 0
    while i < 20:
        yield i
        i += 1


# 2
def only_odd():
    return [n for n in generators_list() if n % 2 == 1]


# 3
def mul_by10():
    return [n * 10 for n in generators_list()]


# 6
def endless(first, last):
    from random import randint

    while True:
        new_last = yield randint(first, last)
        if new_last:
            last = new_last


a = endless(3, 9)

pass
