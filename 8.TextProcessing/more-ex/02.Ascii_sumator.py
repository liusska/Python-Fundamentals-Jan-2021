start_idx = ord(input())
end_idx = ord(input())
text = input()
total_sum = 0
for i in range(len(text)):
    ch = ord(text[i])
    if start_idx < ch < end_idx:
        total_sum += ch

print(total_sum)
