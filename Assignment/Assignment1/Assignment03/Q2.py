my_tuple = (1, 2, 3, 4, 2, 5, 3, 2)
value = int(input("Enter value to find repetition: "))

count = my_tuple.count(value)

if count > 1:
    print(f"{value} is repeated {count} times.")
else:
    print(f"{value} is not repeated.")