percent = int(input())


def solve(number):
    if number == 100:
        print(f"{number}% Complete!")
        print("[%%%%%%%%%%]")
    else:
        expression = "["
        num = number / 10
        for i in range(0, 10):
            if i < num:
                expression += "%"
            else:
                expression += "."
        expression += "]"
        print(f"{number}% {expression}")
        print("Still loading...")


solve(percent)
