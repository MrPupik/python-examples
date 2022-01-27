## steps to build interactive cmd
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
    while not option.isdigit() and (option < 1 or option > 5):
        print("Error: invalid option")
        show_menu(num1, num2)
        option = input()
    return int(option)


def add(num1, num2):
    return f'{str(num1)} + {str(num2)} = {num1+num2}'


def mul(num1, num2):
    return f'{str(num1)} * {str(num2)} = {num1*num2}'


def sub(num1, num2):
    return f'{str(num1)} - {str(num2)} = {num1-num2}'


def get_two_numbers():
    num1 = input("enter first number  ")
    num2 = input("enter second number  ")
    while (not num1.isdigit() or not num2.isdigit()):
        print("Error: not both numbers")
        num1 = input("enter first number  ")
        num2 = input("enter second number  ")
    return (int(num1), int(num2))


def main():
    num1, num2 = get_two_numbers()
    finish = False
    result = ''
    while not finish:
        option = get_option(num1, num2)
        if option == 1:
            result = mul(num1, num2)
        elif option == 2:
            result = add(num1, num2)
        elif option == 3:
            result = sub(num1, num2)
        elif option == 4:
            result = sub(num2, num1)
        else:
            result = "Thank you, have a nice day :)"
            finish = True
        print(result)


main()
