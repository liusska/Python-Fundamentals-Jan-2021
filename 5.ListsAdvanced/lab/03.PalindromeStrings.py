line = input().split(" ")
pall_word = input()
palindrome_list = []

for word in line:
    if word == word[::-1]:
        palindrome_list.append(word)


count = 0
for palindrome in palindrome_list:
    if pall_word == palindrome:
        count += 1

print(palindrome_list)
print(f"Found palindrome {count} times")
