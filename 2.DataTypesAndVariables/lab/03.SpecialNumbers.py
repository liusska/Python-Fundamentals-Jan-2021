n = int(input())

for num in range(1, n + 1):
    sum_of_digit = 0
    digits = num

    while digits > 0:
        sum_of_digit += digits % 10
        digits = int(digits / 10)

    if (sum_of_digit == 5) or (sum_of_digit == 7) or (sum_of_digit == 11):
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")