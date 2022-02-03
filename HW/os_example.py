import os
from threading import main_thread

print(f"current process id is: {os.getpid()}")

print(f"this script file name is {__file__}")
print(f"it is located in {os.path.dirname(__file__)}")

print()
print("create folder structure:")

main_folder = "my_os_example"


if not os.path.exists(main_folder):
    os.mkdir(main_folder)
    os.mkdir(f"{main_folder}\\folder a")
    os.mkdir(f"{main_folder}\\folder b")
    base_path = f"{main_folder}\\folder "
    with open(base_path + "b\\data.dat", "w"):
        pass
    with open(base_path + "b\\data.dat", "w"):
        pass
