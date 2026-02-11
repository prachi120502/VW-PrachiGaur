user_list = input("Enter list elements separated by space: ").split()

print("Alternate elements:")
for i in range(0, len(user_list), 2):
    print(user_list[i], end=" ")