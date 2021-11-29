from test_utils import myTest, TEST_FAILED_EXCEPTION


@myTest(priority=1)
def first_test():
    print("testing, oh thats weird")
    return 1


@myTest(name="good test")
def second_test():
    print("testing...")
    return 0


@myTest
def failed_test():
    print("testing, oh fuck")
    raise TEST_FAILED_EXCEPTION("this is baddd")


if __name__ == "__main__":
    first_test()
    second_test()
    failed_test()