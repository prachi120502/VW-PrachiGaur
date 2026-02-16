List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]

frequency = {}

for num in List1:
    frequency[num] = frequency.get(num, 0) + 1

print(frequency)