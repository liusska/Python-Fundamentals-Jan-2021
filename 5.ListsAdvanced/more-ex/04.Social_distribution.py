populations = [int(x) for x in input().split(", ")]
min_wealth = int(input())
is_distribution_possible = True

for i in range(len(populations)):
    diff = 0
    if populations[i] < min_wealth:
        diff = min_wealth - populations[i]
        populations[i] += diff
    if max(populations) - diff >= min_wealth:
        max_idx = populations.index(max(populations))
        populations[max_idx] -= diff
    else:
        print("No equal distribution possible")
        is_distribution_possible = False
        break

if is_distribution_possible:
    print(f"[{', '.join([str(x) for x in populations])}]")

