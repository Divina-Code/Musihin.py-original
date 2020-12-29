import random
from  random import randint
rand = random.randint(100, 999)

code = str(rand)
game = True

right_number = 0
right_place = 0

while game:
    user_num = (input("Введи трёхзначное чило\t"))
    right_number = 0
    if len(user_num) != 3:
        print("Число не трёх значное")
    elif user_num == code:
        print("Ты угадал")
        game = False
    else:
        for d in code:
            if d in user_num:
                right_number += 1

    print("Ты угадал", right_number, "цифр")



