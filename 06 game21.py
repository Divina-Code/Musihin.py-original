import random
import time
from random import randint as ri
cards_player1 = ri(2,11)
cards_player2 = ri(2,11)
cards_player3 = ri(2,11)
inGame1 = True
inGame2 = True
inGame3 = True
print("Добро пожаловать в игру, парни!")
time.sleep(1)
print("Начинаем")

while not inGame1:
    cardTake1 = str(input("Ну чего ждёшь, ты карту брать будешь?(да или нет)"))
    if cardTake1 == "да":
        cards_player1 += ri(2, 11)
        print("Теперь у тебя очков:", cards_player1)
    elif cardTake1 == "нет":
        inGame1 = False
    else:
        print("Слушай, попроси нормально.")
    if cards_player1 > 21:
        print("Сегодня не твой день")
        inGame1 = False
    if cards_player1 == 21:
        print("Ты победил")
        inGame1 = False
        inGame2 = False
        inGame3 = False
while not inGame2:
    print("X*X" * 5)
    if inGame2:
        cardTake2 = input("Ну чего ждёшь, ты карту брать будешь?(да или нет)")
        if cardTake2 == "да":
            cards_player2 += ri(2, 11)
            print("Теперь у тебя очков:", cards_player2)
        elif cardTake2 == "нет":
            inGame2 = False
        else:
            print("Слушай, попроси нормально.")
    if cards_player2 > 21:
        print("Сегодня не твой день")
        inGame2 = False
    if cards_player2 == 21:
        print("Ты победил")
        inGame1 = False
        inGame2 = False
        inGame3 = False
while not inGame3:
    print("X*X" * 5)
    if inGame3:
        cardTake3 = input("Ну чего ждёшь, ты карту брать будешь?(да или нет)")
        if cardTake3 == "да":
            cards_player3 += ri(2, 11)
            print("Теперь у тебя очков:", cards_player3)
        elif cardTake3 == "нет":
            inGame3 = False
        else:
            print("Слушай, попроси нормально.")
    if cards_player3 > 21:
        print("Сегодня не твой день")
        inGame3 = False
    if cards_player3 == 21:
        print("Ты победил")
        inGame1 = False
        inGame2 = False
        inGame3 = False

