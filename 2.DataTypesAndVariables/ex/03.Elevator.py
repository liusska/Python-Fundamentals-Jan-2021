number_people = int(input())
capacity = int(input())
courses = 0

while number_people > 0:
    if number_people - capacity >= 0:
        number_people -= capacity
        courses += 1
    else:
        if number_people != 0:
            courses += 1
            break

print(courses)