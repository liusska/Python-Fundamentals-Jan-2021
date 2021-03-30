sequence = input().split()
moves = 0


def valid_indexes(index1, index2, data):
    if index1 in range(len(data)) and index2 in range(len(data)) and index1 != index2:
        return True
    return False


def add_additional_elements(mov, data):
    middle = len(data) // 2
    element = f'-{mov}a'
    data.insert(middle, element)
    data.insert(middle + 1, element)
    return data


while True:
    command = input()
    if command == "end":
        break
    moves += 1
    idx1, idx2 = command.split()
    idx1 = int(idx1)
    idx2 = int(idx2)
    if not valid_indexes(idx1, idx2, sequence):
        print("Invalid input! Adding additional elements to the board")
        sequence = add_additional_elements(moves, sequence)
    else:
        if sequence[idx1] == sequence[idx2]:
            element = sequence[idx1]
            print(f"Congrats! You have found matching elements - {element}!")
            sequence.remove(element)
            sequence.remove(element)
        else:
            print("Try again!")

    if not sequence:
        print(f"You have won in {moves} turns!")
        break

if sequence:
    print(f"Sorry you lose :(")
    print(f"{' '.join(sequence)}")