import math

def circle():
    r = float(input("Enter radius: "))
    print("Area:", math.pi * r * r)
    print("Perimeter:", 2 * math.pi * r)

def square():
    s = float(input("Enter side: "))
    print("Area:", s * s)
    print("Perimeter:", 4 * s)

def rectangle():
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    print("Area:", l * b)
    print("Perimeter:", 2 * (l + b))

choice = input("Choose (circle/square/rectangle): ")

if choice == "circle":
    circle()
elif choice == "square":
    square()
elif choice == "rectangle":
    rectangle()
else:
    print("Invalid choice")