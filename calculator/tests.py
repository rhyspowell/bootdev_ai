import sys
import os

sys.path.append(os.getcwd() + "/..")
from functions.run_python_file import run_python_file


def test():
    print("Ran 9 tests")
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)

    result = run_python_file("calculator", "lorem.txt")
    print(result)


if __name__ == "__main__":
    test()
