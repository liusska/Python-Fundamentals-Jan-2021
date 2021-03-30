waiting_people = int(input())
lift_state = [int(x) for x in input().split()]

for i in range(len(lift_state)):
    if lift_state[i] < 4:
        while lift_state[i] < 4 and waiting_people > 0:
            lift_state[i] += 1
            waiting_people -= 1

lift_taken_spots = sum(lift_state)
full_lift = len(lift_state) * 4

if waiting_people == 0 and lift_taken_spots < full_lift:
    print(f"The lift has empty spots!")
elif waiting_people > 0 and lift_taken_spots == full_lift:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
print(' '.join([str(x) for x in lift_state]))