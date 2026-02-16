import random
import string

# Password Generator
length = int(input("Enter password length (8-12): "))

if length < 8:
    length = 8

all_chars = string.ascii_letters + string.digits + "!@#$%^&*"

# Ensure mix of all types
password = [
    random.choice(string.ascii_uppercase),
    random.choice(string.ascii_lowercase),
    random.choice(string.digits),
    random.choice("!@#$%^&*")
]

for _ in range(length - 4):
    password.append(random.choice(all_chars))

random.shuffle(password)
final_password = "".join(password)

print("Generated Password:", final_password)


# CAPTCHA Extension
captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
print("\nCAPTCHA:", captcha)

user_input = input("Retype CAPTCHA: ")

if user_input == captcha:
    print("CAPTCHA Verified Successfully!")
else:
    print("Incorrect CAPTCHA. Try again.")