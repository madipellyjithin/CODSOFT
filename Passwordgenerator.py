import random
import string
print("Welcome to the Password Generator!")
try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 7:
        raise ValueError("Password length must be greater than Eight Characters.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()
use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
char_set = string.ascii_lowercase
if use_uppercase:
    char_set += string.ascii_uppercase
if use_numbers:
    char_set += string.digits
if use_special_chars:
    char_set += string.punctuation
if not char_set:
    print("You must select at least one type of characters to generate a password.")
    exit()
password = ''.join(random.choice(char_set) for _ in range(length))
print(f"Generated password: {password}")
