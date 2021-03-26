n = int(input())
positive = []
negative = []
count_positive = 0
sum_negative = 0
for i in range(0, n):
    number = int(input())
    if number >= 0:
        count_positive += 1
        positive.append(number)
    else:
        negative.append(number)
        sum_negative += number

print(positive)
print(negative)
print(f"Count of positives: {count_positive}. Sum of negatives: {sum_negative}")