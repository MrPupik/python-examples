# steps to build interactive cmd
# setup (like getting first two numbers in first example)
#  main loop - while(not finish)
# show menu
# function for every option
# use user input / data to decide which actions to run
# show menu again
##


# cmd that gets 2 numbers, shows menu that allows user to choose:
# multiply numbers, sum the numbers, first minus last / last minus first

def show_menu(num1=2, num2=1):
    print(f"you entered {num1}, {num2}. choose option:")
    print("   1. multiply")
    print("   2. addition")
    print(f"   3. subtruct {num1} from {num2}")
    print(f"   4. subtruct {num2} from {num1}")
    print(f"   5. exit\n")


def get_option(num1, num2):
    show_menu(num1, num2)
    option = input()
    while (not option.isdigit()) or (int(option) < 1 or int(option) > 5):
        print("Error: invalid option")
        show_menu(num1, num2)
        option = input()
    return int(option)


def str_add(num1, num2):
    return f'{str(num1)} + {str(num2)} = {num1+num2}'


def str_mul(num1, num2):
    return f'{str(num1)} * {str(num2)} = {num1*num2}'


def str_sub(num1, num2):
    return f'{str(num1)} - {str(num2)} = {num1-num2}'


def get_two_numbers():
    num1 = input("enter first number  ")
    num2 = input("enter second number  ")
    while (not num1.isdigit() or not num2.isdigit()):
        print("Error: not both numbers")
        num1 = input("enter first number  ")
        num2 = input("enter second number  ")
    return (int(num1), int(num2))


def two_number_action():
    num1, num2 = get_two_numbers()
    finish = False
    result = ''
    while not finish:
        option = get_option(num1, num2)
        if option == 1:
            result = str_mul(num1, num2)
        elif option == 2:
            result = str_add(num1, num2)
        elif option == 3:
            result = str_sub(num1, num2)
        elif option == 4:
            result = str_sub(num2, num1)
        else:
            result = "Thank you, have a nice day :)"
            finish = True
        print(result)


# two_number_action()


# calculator


def add(num1, num2):
    return num1+num2


def mul(num1, num2):
    return num1*num2


def sub(num1, num2):
    return num1-num2


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

    # check it is a number
    # return it
    pass


def calculator_main_loop():
    finish = False
    result = 0
    new_result = None
    while not finish:
        option = get_option()
        print("option is: ", option)
        if option == 5:
            finish = True
            print("love you, bye")
            continue
        else:
            number = get_number()
        if option == 1:
            new_result = add(result, number)
            print(f'{result} + {number} = {new_result}')
        elif option == 2:
            new_result = sub(result, number)
            print(f'{result} - {number} = {new_result}')
        elif option == 3:
            new_result = mul(result, number)
            print(f'{result} * {number} = {new_result}')
        elif option == 4:
            new_result = divide(result, number)
            print(f'{result} / {number} = {new_result}')

        result = new_result


calculator_main_loop()
