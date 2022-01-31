from platform import system
from subprocess import run

# function as object, subprocess


def run_command(command: str):
    try:
        return run(command, shell=True)
    except Exception as e:
        print("err occured:\n" + str(e))


def win_listAllDir():
    run_command("dir")


def linux_listAllDir():
    run_command("ls")


listAllDir = {"Linux": linux_listAllDir, "Windows": win_listAllDir}


if __name__ == "__main__":
    listAllDir[system()]()
