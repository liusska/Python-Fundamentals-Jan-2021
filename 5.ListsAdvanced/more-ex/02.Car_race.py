total_time = [float(x) for x in input().split()]
finish_index = len(total_time) // 2
left_racer = total_time[:finish_index]
right_racer = total_time[finish_index+1:]
left_racer_time = 0
right_racer_time = 0

for i in range(len(left_racer)):
    if left_racer[i] == 0:
        left_racer_time *= 0.8
    left_racer_time += left_racer[i]

for i in range(len(right_racer)-1, -1, -1):
    if right_racer[i] == 0:
        right_racer_time *= 0.8
    right_racer_time += right_racer[i]

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
