rooms = int(input())
free_chairs = 0
enough_chairs = True
for room in range(1, rooms + 1):
    [chairs, taken_chairs] = input().split(" ")
    chairs = len(chairs)
    taken_chairs = int(taken_chairs)
    if chairs < taken_chairs:
        enough_chairs = False
        print(f"{taken_chairs - chairs} more chairs needed in room {room}")
    else:
        current_free_chairs = chairs - taken_chairs
        free_chairs += current_free_chairs

if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")