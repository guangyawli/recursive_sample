# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


def recursive(n):
    if n == 1:
        return 1
    else:
        return n*recursive(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 預設 recursion 次數
    print('Python 預設 recursion 次數 : \n' + str(sys.getrecursionlimit()))
    print('')
    # 階乘
    print('階乘:')
    ans = recursive(5)
    print(ans)

    # Fibonacci
    print('')
    print('Fibonacci 數列:')
    print(fibonacci(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
