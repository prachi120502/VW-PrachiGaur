# Program for 4 digit number operations

num = int(input("Enter a 4 digit number: "))

d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10

# a) Face value
print("Face values:", d1, d2, d3, d4)

# b) Place value
print("Place values:")
print(f"{num} = {d1*1000} + {d2*100} + {d3*10} + {d4}")

# c) Reverse number
reverse = d4*1000 + d3*100 + d2*10 + d1
print("Reverse number:", reverse)