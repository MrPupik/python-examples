import sys


if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[2].isdigit():
        print(
            "wrong parameters, pleas enter python sys_example {string} {number-of-times}"
        )
        sys.exit(1)
    st, times = sys.argv[1:]
    print(st * int(times))

    print(f"current platform is {sys.platform}")

    print(f"this python is located at {sys.executable}")
    print(f"this python is located at {sys.path}")
