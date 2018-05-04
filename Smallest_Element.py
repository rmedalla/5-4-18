numbers = [-1, 1, 4, 2, 15, 7, -4, 8]

smallest_num = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] < smallest_num:
        smallest_num = numbers[i]

print(smallest_num)
