# Temperature conversion program

choice = input("Enter C to convert Celsius to Fahrenheit or F to convert Fahrenheit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print("Temperature in Fahrenheit =", fahrenheit)

elif choice.upper() == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print("Temperature in Celsius =", celsius)

else:
    print("Invalid choice")