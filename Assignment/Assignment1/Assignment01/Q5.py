# Function to find maximum of three numbers

def find_max(a, b, c):
    return max(a, b, c)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("Maximum number is:", find_max(x, y, z))