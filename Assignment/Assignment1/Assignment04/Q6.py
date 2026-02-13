text = """Python is a high-level, general-purpose programming language.
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically typed and garbage-collected.
It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

# Convert to lowercase
text = text.lower()

letter_count = {}

for char in text:
    if char.isalpha():   # Only count letters
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

# Print result in sorted order
for key in sorted(letter_count):
    print(key, ":", letter_count[key])