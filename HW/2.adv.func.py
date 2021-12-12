# 1
def mulBy(multiplier):
    def result_function(num):
        return result * num

    return result_function


# 2
def myzip(it1, it2):
    for i in range(min([len(it1), len(it2)])):
        yield (it1[i], it2[i])


# 3
def genfilterby(num):
    def filter(iter):
        return [n for n in iter if n % num == 0]

    return filter
