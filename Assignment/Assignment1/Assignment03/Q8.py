people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}

# A. Number of students
print("Total students:", len(people))

# B. Change Lisa’s colour
people['Lisa'] = 'Green'

# C. Remove Jenny
people.pop('Jenny')

# D. Sort and print
for name in sorted(people):
    print(name, ":", people[name])