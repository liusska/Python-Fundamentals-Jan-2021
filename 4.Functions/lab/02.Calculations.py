operation = input()
first_num = int(input())
second_num = int(input())


def calculations(op, num1, num2):
    if operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 // num2
    elif operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2


print(calculations(operation, first_num, second_num))
