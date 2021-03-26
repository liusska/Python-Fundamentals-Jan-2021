first = int(input())
second = int(input())


def factorial(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact


first_fact = factorial(first)
second_fact = factorial(second)

result = first_fact / second_fact

print(f"{result:.2f}")