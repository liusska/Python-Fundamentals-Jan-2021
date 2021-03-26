number = input()


def odd_even_nums(num):
    even = 0
    odd = 0
    for ch in num:
        num = int(ch)
        if num % 2 == 0:
            even += num
        else:
            odd += num
    return f"Odd sum = {odd}, Even sum = {even}"


print(odd_even_nums(number))