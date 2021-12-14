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


def avg(lst):
    if lst:
        return sum(lst) / len(lst)


def get_nums():
    # num = None
    lst = []
    num = input("enter num\n")
    while num != "finish":
        lst.append(int(num))
        num = input("enter num\n")

    return lst


def manager():
    lst = get_nums()
    print(avg(lst))


manager()
