import random
import string
def generate_password(length, name):
    # Ensure the password is at least 8 characters long
    if length < 8:
        length = 8
    
    # Include the name in the password
    password = name
    
    # Add random characters to meet the length requirement
    while len(password) < length:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    
    # Shuffle the password to mix up the characters
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

name = input("Enter your name: ")
password_length = int(input("Enter the minimum length of the password (minimum 8 characters): "))

print("Your random password based on your name is:", generate_password(password_length, name))
