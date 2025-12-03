import random
import string

length = int(input("Enter password length: "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = string.punctuation

password_chars = []
password_chars.append(random.choice(uppercase))
password_chars.append(random.choice(lowercase))
password_chars.append(random.choice(digits))
password_chars.append(random.choice(special))

all_chars = uppercase + lowercase + digits + special
for i in range(length - 4):
    password_chars.append(random.choice(all_chars))

random.shuffle(password_chars)
password = "".join(password_chars)

print(f"\nGenerated Password: {password}")

import random, string

password = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 10))
print("Generated Password:", password)
