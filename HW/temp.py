def add(num1, num2):
    return num1 + num2


def mul(num1, num2):
    return num1 * num2


def sub(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def show_menu():
    print(f"choose action:")
    print("   1. add")
    print("   2. subtruct")
    print("   3. multiply")
    print("   4. divide")
    print("   5. exit\n")


def get_option():
    show_menu()
    option = input()
    while (not option.isdigit()) or (int(option) < 1 or int(option) > 5):
        print("Error: invalid option")
        show_menu()
        option = input()
    return int(option)


# main loop - calc every user choi


def get_number():
    number = input("enter number ")
    while not number.isdigit():
        print("error: not a number")
        number = input("enter number ")
    return int(number)


def calculator_main_loop():
    finish = False
    result = 0
    while not finish:
        option = get_option()

        if option == 5:
            finish = True
            print(f"Love you, bye")
            continue
        else:
            number = get_number()

        if option == 1:
            new_result = add(result, number)
            print(f"{result} + {number} = {new_result}")
        elif option == 2:
            new_result = sub(result, number)
            print(f"{result} - {number} = {new_result}")
        elif option == 3:
            new_result = mul(result, number)
            print(f"{result} * {number} ={new_result}")
        elif option == 4:
            new_result = divide(result, number)
            print(f"{result} / {number} = {new_result}")

        result = new_result


calculator_main_loop()
