import time
import random
from random import randint

card_player1 = random.randint(2, 11)
card_player2 = random.randint(2, 11)
card_player3 = random.randint(2, 11)
y = 1
Vowdas = False
while Vowdas != True:
    while card_player1 != 0:
        print("Хочешь взять карту, игрок 1? P.s. введи Yes или No")

        c = str(input())
        if c == "Yes":
            print("Держи")
            card_player1 += random.randint(2, 11)
            if card_player1 > 21:
                print("Сегодня не твой день, чел")
                card_player1 = 0
            if card_player1 == 21:
                print("Мои поздравления, ты выиграл! ")
                Vowdas = True
            if card_player1 < 21:
                print("Сиди и жди")
        if c == "No":
            print("На нет и суда нет")

    print("Следующий")
    print("Хочешь взять карту, игрок 2? P.s. введи Yes или No")
    v = str(input())
    if v == "Yes":
        print("Держи")
        card_player2 += random.randint(2, 11)
        if card_player2 > 21:
            print("Сегодня не твой день, чел")
            card_player2 = 0
        if card_player2 == 21:
            print("Мои поздравления, ты выиграл! ")
            Vowdas = True
        if card_player2 < 21:
            print("Сиди и жди")
    if v == "No":
        print("На нет и суда нет")
    if (c == "No" and v == "No") or (card_player2 == 0 and card_player1 == 0):
        print("Игрок 3, ты выиграл")
    print("Следующий")
    print("Хочешь взять карту, игрок 3? P.s. введи Yes или No")
    b = str(input())
    if b == "Yes":
        print("Держи")
        card_player3 += random.randint(2, 11)
        if card_player3 > 21:
            print("Сегодня не твой день, чел")
            card_player3 = 0
        if card_player3 == 21:
            print("Мои поздравления, ты выиграл! ")
            Vowdas = True
        if card_player3 < 21:
            print("Сиди и жди")
    if b == "No":
        print("На нет и суда нет")
