
my_dict = {}


def input_int(num_range: tuple):
    """
    `range`: tuple like (from, to)
    """
    frm, to = num_range
    option = input(f'enter number between {frm} and {to} ')
    while (not option.isdigit()) or (int(option) < frm or int(option) > to):
        print("Error: invalid option")
        option = input()
    return int(option)


def cool():
    print('yoyo wshtasupp')


if __name__ == '__main__':
    print("code running....")
