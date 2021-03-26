players = {}
total_points = {}


def add_player(name, place, points, player_position_skill):
    if name not in player_position_skill:
        player_position_skill[name] = {place: points}
        total_points[name] = points
    else:
        if place not in player_position_skill[name]:
            player_position_skill[name][place] = points
            total_points[name] += points
        else:
            if player_position_skill[name][place] < points:
                player_position_skill[name][place] = points
                total_points[player] -= total_points[player]
                total_points[name] += points
    return player_position_skill


def duel(player_1, player_2, player_position_skill):
    dict1 = {}
    dict2 = {}
    if player_1 in players and player_2 in players:
        for key, value in player_position_skill.items():
            if key == player_1:
                for position, points in value.items():
                    dict1[position] = points
            elif key == player_2:
                for position, points in value.items():
                    dict2[position] = points

        for p, s in dict1.items():
            if p in dict2:
                if dict1[p] > dict2[p]:
                    del player_position_skill[player_2]
                    del total_points[player_2]
                    break
                elif dict2[p] > dict1[p]:
                    del player_position_skill[player_1]
                    del total_points[player_1]
                    break
    return players


while True:
    line = input()
    if line == 'Season end':
        break
    if '->' in line:
        tokens = line.split(' -> ')
        player = tokens[0]
        position = tokens[1]
        skill = int(tokens[2])
        players = add_player(player, position, skill, players)
    elif 'vs' in line:
        tokens = line.split(' vs ')
        player1 = tokens[0]
        player2 = tokens[1]
        players = duel(player1, player2, players)

total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
for player, points in total_points.items():
    print(f'{player}: {points} skill')
    for key, value in players.items():
        value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
        if player == key:
            for position, skill in value.items():
                print(f'- {position} <::> {skill}')
