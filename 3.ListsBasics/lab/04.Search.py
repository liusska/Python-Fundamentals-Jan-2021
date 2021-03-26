n = int(input())
word = input()

all_inputs = []
filter_input = []

for i in range(0, n):
    current_input = input()
    all_inputs.append(current_input)
    if word in current_input:
        filter_input.append(current_input)

print(all_inputs)
print(filter_input)