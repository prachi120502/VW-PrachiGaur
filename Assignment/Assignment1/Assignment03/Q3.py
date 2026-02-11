my_list = [10, 20, 30, (40, 50), 60]

count = 0

for item in my_list:
    if isinstance(item, tuple):
        break
    count += 1

print("Count:", count)