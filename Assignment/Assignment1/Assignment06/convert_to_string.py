list_nums = [1, 2, 3]
tuple_nums = (4, 5, 6)

result = list(map(str, list_nums)) + list(map(str, tuple_nums))

print(result)