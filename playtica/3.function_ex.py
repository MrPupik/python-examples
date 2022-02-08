"""
1. ---
2. --- 
3. exit """
from re import compile


def print_menu():
    print('choose your option: "+" | "-" | "x" for exit')


def get_user_option():
    option = input('\n')
    while (not option.isdigit() or int(option) > 3 or int(option) < 1):
        print('Error: wrong input')
        option = input()
    return int(option)


def get_user_sign():
    options = input()
    if 'x' in options:
        return False

    reg = compile('[+-x] \d+')
    while (not reg.search(options)):
        print('Error: wrong input')
        options = input()
    op, num = options.split()
    return op, int(num)


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1-num2


actions = {
    '+': add,
    '-': sub
}


def calculator_main_loop():
    finish = False
    print("@@@@@@ welcom to calc ! @@@@@@")
    result = 0
    while not finish:
        print_menu()
        user_input = get_user_sign()
        if not user_input:
            finish = True
            continue

        option, number = user_input
        new_result = actions[option](result, number)
        print(f"{result} {option} {number} = {new_result}")
        result = new_result

    print("bye")


calculator_main_loop()
