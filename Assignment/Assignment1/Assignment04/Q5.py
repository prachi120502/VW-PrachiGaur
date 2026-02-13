# Take input
user_string = input("Enter a string: ")

# Convert to list
char_list = list(user_string)

unique_chars = []

for ch in char_list:
    if ch not in unique_chars:
        unique_chars.append(ch)

print("Unique characters:", unique_chars)