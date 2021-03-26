command = input()

coffee_count = 0

while command != "END":
    if command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie" or command.lower() == "coding":
        if command.isupper():
            coffee_count += 2
        elif command.islower():
            coffee_count += 1

    command = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)