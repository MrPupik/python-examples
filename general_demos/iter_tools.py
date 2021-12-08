from itertools import accumulate, chain, combinations, compress
from operator import mul


def printer(itr):
    print(list(itr))


a = [1, 2, 3]
b = [3, 4, 5]
printer(accumulate([1, 2, 3]))
printer(accumulate([2, 3], mul))
printer(chain(a, b))  # like +, but creates iterator
printer(combinations(a + b, 2))
printer(compress(a + b, [a % 2 == 0 for a in a + b]))
