experience = float(input())
battles_count = int(input())
total_battle_experience = 0
successful_battles = 0

for i in range(1, battles_count + 1):
    current_exp = float(input())
    total_battle_experience += current_exp
    if i % 3 == 0:
        total_battle_experience += current_exp * 0.15
    if i % 5 == 0:
        total_battle_experience -= current_exp * 0.10
    if i % 15 == 0:
        total_battle_experience += current_exp * 0.05
    successful_battles += 1
    if total_battle_experience >= experience:
        break

if total_battle_experience >= experience:
    print(f"Player successfully collected his needed experience for {successful_battles} battles.")
else:
    needed_exp = experience - total_battle_experience
    print(f"Player was not able to collect the needed experience, {needed_exp:.2f} more needed.")