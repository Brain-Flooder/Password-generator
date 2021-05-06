import random
a=input("Number of Password: ")
a=int(a)
b=input("Password length: ")
b=int(b)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}\|;:,./<>?"
for p in range(a):
    password = ''
    for c in range(b):
        password+=random.choice(chars)
    print('Your password is '+password)