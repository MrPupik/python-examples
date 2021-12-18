import sys
from typing import Type
import warnings

print("this is normal print")
sys.stderr.writelines(["this is an error"])
warnings.warn("this is a warning")


def risky_operation():
    from random import randint
    if randint(0, 100) > 25:
        raise ValueError("i'm sorry, this is too high for me")
    return True


try:
    risky_operation()
    print("oh great we made it")
except ValueError as err:
    print("oh well")
    print(err)
finally:
    print("cleaning up")


print("this will happn only if we made it ")
