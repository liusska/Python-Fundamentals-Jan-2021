num1 = int(input())
num2 = int(input())
num3 = int(input())


def sum_numbers(n1, n2):
    return n1 + n2


def subtract(func, n3):
    return func - n3


def add_and_subtract(n1, n2, n3):
    return subtract(sum_numbers(n1, n2), n3)


print(add_and_subtract(num1, num2, num3))


