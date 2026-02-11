my_list = ['a', 'b', 'c', 'd', 'e']

index = my_list.index('b')
my_list[index:index+1] = [1, 2, 3]

print("Updated list:", my_list)