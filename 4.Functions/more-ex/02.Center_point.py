def find_closest_points(x_1, y_1, x_2, y_2):
    first_result = abs(x_1) + abs(y_1)
    second_result = abs(x_2) + abs(y_2)
    if first_result < second_result:
        print(f"({int(x_1)}, {int(y_1)})")
    else:
        print(f"({int(x_2)}, {int(y_2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

find_closest_points(x1, y1, x2, y2)