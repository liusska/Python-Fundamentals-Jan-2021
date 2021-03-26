cards = input().split(" ")
terminated = False
players_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
players_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for card in cards:
    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])
    if team == "A":
        if player not in players_a:
            continue
        else:
            players_a.remove(player)
            if len(players_a) < 7:
                terminated = True
                break
    elif team == "B":
        if player not in players_b:
            continue
        else:
            players_b.remove(player)
            if len(players_b) < 7:
                terminated = True
                break

print(f"Team A - {len(players_a)}; Team B - {len(players_b)}")
if terminated:
    print("Game was terminated")