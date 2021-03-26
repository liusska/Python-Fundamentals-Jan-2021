def add_piece(list_pieces, name_to_add, composer_to_add, key_to_add):
    searched_piece = [p for p in list_pieces if p.name == name_to_add]
    if searched_piece:
        return f"{name_to_add} is already in the collection!"
    piece_to_add = Piece(name_to_add, composer_to_add, key_to_add)
    pieces.append(piece_to_add)
    return f"{name_to_add} by {composer_to_add} in {key_to_add} added to the collection!"


def remove_piece(list_pieces, piece_to_remove):
    searched_piece = [p for p in list_pieces if p.name == piece_to_remove]
    if searched_piece:
        pieces.remove(searched_piece[0])
        return f"Successfully removed {piece_to_remove}!"
    return f"Invalid operation! {piece_to_remove} does not exist in the collection."


def change_key(list_pieces, piece_name, new_key):
    searched_piece = [p for p in list_pieces if p.name == piece_name]
    if searched_piece:
        searched_piece[0].key = new_key
        return f"Changed the key of {piece_name} to {new_key}!"
    return f"Invalid operation! {piece_name} does not exist in the collection."


class Piece:
    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key

    def __repr__(self):
        return f"{self.name} -> Composer: {self.composer}, Key: {self.key}"


pieces = []
n = int(input())
for _ in range(n):
    piece, composer, key = input().split("|")
    new_piece = Piece(piece, composer, key)
    pieces.append(new_piece)

while True:
    command = input()
    if command == "Stop":
        break
    tokens = command.split("|")

    if tokens[0] == "Add":
        piece = tokens[1]
        composer = tokens[2]
        key = tokens[3]
        print(add_piece(pieces, piece, composer, key))
    elif tokens[0] == "Remove":
        piece = tokens[1]
        print(remove_piece(pieces, piece))
    elif tokens[0] == "ChangeKey":
        piece = tokens[1]
        key = tokens[2]
        print(change_key(pieces, piece, key))

sorted_pieces = sorted(pieces, key=lambda p: (p.name, p.composer))
for piece in sorted_pieces:
    print(piece)