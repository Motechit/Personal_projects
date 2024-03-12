#Let's build a random password generator

import random
import string

def generate_password(length):
    #define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    #generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

#lets now generate a password of length 15
password = generate_password(12)
print("Generated password:", password)
