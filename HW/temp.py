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


def caclulator_main_loop():
    finish = False
    result = 0
    while not finish:
        option = get_option()
        if option == 1:
            print(f'{result} + ')
        
