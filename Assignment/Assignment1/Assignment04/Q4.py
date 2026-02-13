# List of lambda functions
conversions = [
    lambda t: t * 1000,             # tonnes to kg
    lambda kg: kg * 1000,           # kg to grams
    lambda g: g * 1000,             # grams to mg
    lambda mg: mg * 0.00000220462   # mg to pounds
]

# Take input from user
tonnes = float(input("Enter weight in tonnes: "))

# Perform conversions
kg = conversions[0](tonnes)
grams = conversions[1](kg)
mg = conversions[2](grams)
lbs = conversions[3](mg)

print("Kilograms:", kg, "kg")
print("Grams:", grams, "gm")
print("Milligrams:", mg, "mg")
print("Pounds:", lbs, "lbs")