from types import FunctionType


class TEST_FAILED_EXCEPTION(Exception):
    pass


def myTest(func=None, name=None, priority=3) -> FunctionType:
    """
    my super smart decorator
    """
    myFunc = func

    def generic_wrapper(func, *args, **kwargs):
        print("wrapper running")
        test_name = name if name else func.__name__
        print(f"runnig test {test_name}")
        result = 0
        try:
            result = func(*args, **kwargs)
        except TEST_FAILED_EXCEPTION as e:
            print(f"-x- test {test_name} failed")
            print(str(e))
        else:
            if result != 0 and priority < 3:
                print(f"-?- something went wrong with {test_name}, check the log")
            else:
                print(f"-v- test {test_name} passed !")

    def outer_wrapper(*args, **kwargs):
        generic_wrapper(myFunc, *args, **kwargs)

    # make a decorator that is considering the params
    def decorator(func):
        def inner_wrapper(*args, **kwargs):
            generic_wrapper(func, *args, **kwargs)

        return inner_wrapper

    if myFunc is not None:
        # im a decorator
        return outer_wrapper
    else:
        # im a decorator factory
        return decorator


def ProgressBar(func):
    prog_char = "#"

    def decorator(*args, **kwargs):
        result = func(*args, **kwargs)
        print(prog_char, end="", flush=True)
        return result

    return decorator


@ProgressBar
def slow_func():
    from time import sleep

    sleep(0.5)


if __name__ == "__main__":
    print("running:")
    for i in range(20):
        slow_func()
