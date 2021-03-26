def find_closest_points(x_1, y_1, x_2, y_2, a_1, b_1, a_2, b_2):
    first_result = abs(x_1) + abs(y_1)
    second_result = abs(x_2) + abs(y_2)
    third_result = abs(a_1) + abs(b_1)
    fourth_result = abs(a_2) + abs(b_2)
    if first_result + second_result > third_result + fourth_result:
        if first_result > second_result:
            print(f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})")
        else:
            print(f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})")
    else:
        if third_result > fourth_result:
            print(f"({int(a_2)}, {int(b_2)})({int(a_1)}, {int(b_1)})")
        else:
            print(f"({int(a_1)}, {int(b_1)})({int(a_2)}, {int(b_2)})")


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

find_closest_points(x1, y1, x2, y2, a1, b1, a2, b2)