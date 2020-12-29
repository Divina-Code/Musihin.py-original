import random

lol = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
length = int(input('длина пароля?'+ "\n"))

password =''
for i in range(length):
    password += random.choice(lol)
print(password)
