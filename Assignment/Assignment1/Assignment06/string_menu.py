text = input("Enter string: ")

print("A. Even Position")
print("B. Odd Position")
print("C. Length")
print("D. Add 'a' length times")

choice = input("Choose option: ")

if choice == "A":
    print(text[1::2])
elif choice == "B":
    print(text[0::2])
elif choice == "C":
    print(len(text))
elif choice == "D":
    print(text + "a" * len(text))
else:
    print("Invalid option")