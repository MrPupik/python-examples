from getpass import getpass
from pprint import pprint

####################### user mangment #######################


users = {
    "master": {"role": "admin", "password": "mrBin", "ip": "192.168.1.2"},
    "user1": {"role": "user", "password": "1234", "ip": "192.168.1.3"},
}


def show_menu():
    print(f"choose action:")
    print("   1. add user")
    print("   2. delete user")
    print("   3. change password")
    print("   4. list all users")
    print("   5. exit\n")


def get_option():
    show_menu()
    option = input()
    while (not option.isdigit()) or (int(option) < 1 or int(option) > 5):
        print("Error: invalid option")
        show_menu()
        option = input()
    return int(option)


def log_in(user):
    """logges in the user"""
    pwd = input("to access user mangaer, type admin password: ")
    admin_pass = user["password"]
    for i in range(3, 0, -1):
        if pwd == admin_pass:
            return True
        print(f"wrong password. {i} attempts remaining...")
        pwd = input("type admin password: ")

    return False


def add_user_with_help():
    global users
    print("\n@ add user @")
    help_str = """user format:
             username|password|role|ip_ddress
        ^       ^       ^         ^
       any     any   user/admin   XXX.XXX.XXX.XXX
 for example: 'user1|0000|user|127.0.0.1'"""
    user_data = new_user_input_validation()
    while not (user_data):
        print(help_str)
        user_data = new_user_input_validation()
    new_user = {"password": user_data[1],
                "role": user_data[2], "ip": user_data[3]}
    users[user_data[0]] = new_user
    print("user added succefully")


def new_user_input_validation():
    raw_data = input("enter user details, for help enter '?': ")
    data = raw_data.split("|")
    if len(data) != 4:
        return
    if data[2] not in ("user", "admin"):
        return
    ip_nums = data[3].split(".")
    if len(ip_nums) != 4 or False in [num.isdigit() for num in ip_nums]:
        return
    if data[0] in users.keys():
        print("username is taken")
        return
    return data


def add_user():
    data = 'popo|1234|user|1.1.1.1'  # data = input('enter new user details: ')
    data_lst = data.split('|')  # [popo, 1234, user, 1.1.1.1]

    # how to add to users dictionary?
    user_name = data_lst[0]  # popo
    user_data = {'password': data_lst[1],
                 'role': data_lst[2], 'ip': data_lst[3]}
    # users['popo'] = {'password': 1234, 'role': 'user', 'ip': '1.1.1.1'}
    users[user_name] = user_data
    print(f'user {user_name} added succesfully')


def delete_user():
    name = input('enter user name to delete: ')
    if name not in users.keys():
        print('no such user')
    else:
        users.pop(name)


def set_user_password():
    name = input('enter user name: ')
    new_password = input('enter new password: ')
    if name not in users.keys():
        print('no such user')
    else:
        users[name]['password'] = new_password


def user_manager_main_loop():
    global users
    admin_user = users['master']
    if not log_in(admin_user):
        print("-xx- log in failed. -xx-")
        return None
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@ welcome to user manager @@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("good evening, master")

    finish = False
    while not finish:
        option = get_option()
        if option == 5:
            print('bye')
            finish = True

        if option == 1:
            add_user()
        if option == 2:
            delete_user()
        if option == 3:
            set_user_password()
        if option == 4:
            print('@ all users @')
            pprint(users)


user_manager_main_loop()
