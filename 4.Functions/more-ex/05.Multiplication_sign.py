def multiplication_sign(n1, n2, n3):
    count_positive = 0
    if n1 == 0 or n2 == 0 or n3 == 0:
        return -1
    if n1 > 0:
        count_positive += 1
    if n2 > 0:
        count_positive += 1
    if n3 > 0:
        count_positive += 1
    return count_positive


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = multiplication_sign(num1, num2, num3)
if result == -1:
    print("zero")
elif result % 2 == 0:
    print("negative")
else:
    print("positive")