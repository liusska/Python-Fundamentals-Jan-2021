import re

pattern = r"([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)"
data = input()
matches = re.findall(pattern, data)

cool_threshold = 1
for word in data:
    for ch in word:
        if ch.isdigit():
            cool_threshold *= int(ch)


emoji_count = len(matches)
coolness_emoji = []

for match in matches:
    current_coolness = 0
    for ch in match[1]:
        current_coolness += ord(ch)
    if current_coolness >= cool_threshold:
        coolness_emoji.append(''.join(match))

print(f"Cool threshold: {cool_threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for em in coolness_emoji:
    print(em)