import time
import random
from random import randint

player1 = random.randint(2, 11)
player2 = random.randint(2, 11)
player3 = random.randint(2, 11)

inGame1 = True
inGame2 = True
inGame3 = True

print("Игрок 1, твой счёт: ", player1)
time.sleep(1)
print("Игрок 2, твой счёт: ", player2)
time.sleep(1)
print("Игрок 3, твой счёт: ", player3)
time.sleep(1)

while inGame1 or inGame2 or inGame3:
    if inGame1:
        print("****************************")
        answer1 = input("Игрок 1, будешь карту брать? (напиши по русски и без пробелов)").lower()
        if answer1 == "да":
            print("Ну бери")
            player1 += randint(2, 11)
            time.sleep(1)
            print("Твой счёт: ", player1)
        if player1 > 21:
            time.sleep(1)
            print("Сегодня точно не твой день")
            inGame1 = False
        if player1 == 21:
            time.sleep(1)
            print("Тебе повезло и ты выиграл")
            inGame2 = False
            inGame3 = False
        elif answer1 == "нет":
            time.sleep(1)
            print("Ну не хочешь и ладно, мне больше останется")
            inGame2 = False
        elif answer1 != "да" and answer1 != "нет":
            print("Я же сказал нормально напиши, да или нет. Следующий")
            time.sleep(1)
    if inGame2:
        print("****************************")
        answer2 = input("Игрок 2, будешь карту брать? (напиши по русски и без пробелов)").lower()
        if answer2 == "да":
            print("Ну бери")
            player2 += randint(2, 11)
            time.sleep(1)
            print("Твой счёт: ", player2)
            if player2 > 21:
                time.sleep(1)
                print("Сегодня точно не твой день")
                inGame2 = False
            if player2 == 21:
                time.sleep(1)
                print("Тебе повезло и ты выиграл")
                inGame1 = False
                inGame3 = False
        elif answer2 == "нет":
            time.sleep(1)
            print("Ну не хочешь и ладно, мне больше останется")
            inGame2 = False
        elif answer2 != "да" and answer2 != "нет":
            print("Я же сказал нормально напиши, да или нет. Следующий")
            time.sleep(1)
    if inGame3:
        print("****************************")
        answer3 = input("Игрок 3, будешь карту брать? (напиши по русски и без пробелов)").lower()
        if answer3 == "да":
            print("Ну бери")
            player3 += randint(2, 11)
            time.sleep(1)
            print("Твой счёт: ", player2)
            if player3 > 21:
                time.sleep(1)
                print("Сегодня точно не твой день")
                inGame3 = False
            if player3 == 21:
                time.sleep(1)
                print("Тебе повезло и ты выиграл")
                inGame1 = False
                inGame2 = False
        elif answer3 == "нет":
            time.sleep(1)
            print("Ну не хочешь и ладно, мне больше останется")
            inGame3 = False
        elif answer3 != "да" and answer3 != "нет":
            print("Я же сказал нормально напиши, да или нет. Следующий")
            time.sleep(1)
    if inGame1 == False and inGame2 == False and inGame3 != 21:
        print("Игрок 3, ты выиграл")
        inGame1 = False
        inGame2 = False
        inGame3 = False
    if inGame1 == False and inGame3 == False and inGame2 != 21:
        print("Игрок 2, ты выиграл")
        inGame1 = False
        inGame2 = False
        inGame3 = False
    if inGame2 == False and inGame3 == False and inGame1 != 21:
        print("Игрок 1, ты выиграл")
        inGame1 = False
        inGame2 = False
        inGame3 = False

if 21 >= player1 > player2 and 21 >= player1 > player3 and inGame1 == True:
    print("Игрок 1 победил")
elif 21 >= player2 > player1 and 21 >= player2 > player3 and inGame2 == True:
    print("Игрок 2 победил")
elif 21 >= player3 > player1 and 21 >= player3 > player2 and inGame3 == True:
    print("Игрок 2 победил")
elif player1 > 21 and player2 > 21 and player3 > 21:
    print("Нет победителей")

