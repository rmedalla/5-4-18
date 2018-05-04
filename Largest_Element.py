numbers = [-1, 1, 4, 2, 15, 7, -4, 8]

largest_num = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > largest_num:
        largest_num = numbers[i]

print(largest_num)


        