n = int(input())
for _ in range(n):
    line = input()
    word_start_idx = line.index("@")
    word_end_idx = line.index("|")
    name = line[word_start_idx+1:word_end_idx]
    age_start_idx = line.index("#")
    age_end_idx = line.index("*")
    age = line[age_start_idx+1:age_end_idx]
    print(f"{name} is {age} years old.")
