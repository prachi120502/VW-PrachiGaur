numbers = []
for i in range(6):
    numbers.append(int(input("Enter number: ")))

result = {"EVEN": [], "ODD": []}

for num in numbers:
    if num % 2 == 0:
        result["EVEN"].append(num)
    else:
        result["ODD"].append(num)

print(result)