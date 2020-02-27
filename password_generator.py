import random

password_file = open("passwords.txt", 'r')
passwords = password_file.readlines()
for index in range (0,10000):
    #index = random.randint(0, len(passwords))
    if 'jacob' in passwords[index] or 'jake' in passwords[index]:
        print(f"password number {index}: {passwords[index]}")
