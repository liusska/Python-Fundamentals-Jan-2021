def tribonacci_sequence(n):
    list_of_sequences = []
    list_of_sequences.append(1)
    for _ in range(n-1):
        current_num = 0
        for i in range(len(list_of_sequences)):
            if i < 3:
                current_num += list_of_sequences[i]
            else:
                current_num += list_of_sequences[i-2]
                current_num += list_of_sequences[i-1]
        list_of_sequences.append(current_num)
    print(' '.join([str(x) for x in list_of_sequences]))


n = int(input())

tribonacci_sequence(n)
