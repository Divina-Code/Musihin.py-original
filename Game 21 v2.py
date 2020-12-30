from random import randint

player1 = randint(2, 11) #Счёт игрока (очки)
player2 = randint(2, 11)

print("Player1, your score is:", player1)
print("Player2, your score is:", player2)

inGame1 = True #Играт ли игрок1 или уже закончил
inGame2 = True #Играт ли игрок1 или уже закончил



while inGame1 or inGame2:
    print("#"*50)
    #ПРЕДЛАГАЕМ КАРТУ 1-МУ игроку
    if inGame1:
        take_card = input("Player1,  Будешь брать карту? [ДА\НЕТ]")
        if take_card == "ДА":
            player1+=randint(2, 11)
            print("Теперь у тебя очков", player1)
        elif take_card =="НЕТ":
            inGame1 = False
        else:
            print("Я тебя не понял")

    #Предлагаем карту 2-му игроку
    #ПРЕДЛАГАЕМ КАРТУ 1-МУ игроку
    if inGame2:
        take_card = input("Player2, Будешь брать карту? [ДА\НЕТ]")
        if take_card == "ДА":
            player2+=randint(2, 11)
            print("Теперь у тебя очков", player2)
        elif take_card =="НЕТ":
            inGame2 = False
        else:
            print("Я тебя не понял")

###############################################################
    #Проверяем, не перебрал ли игрок карт
    if player1>=21:
        inGame1 = False

    #Проверяем, не перебрали ли второй игрок карт
    if player2>=21:
        inGame2 = False

print("Игра окончена")

#ИЩЕМ ПОБЕДИТЕЛЯ
if player1 <= 21 and player1>player2:
    print("Player1 победил! Ура!")
elif player2 <=21 and player2>player1:
    print("player2 win")
elif player1 >21 and player2>21:
    print("нет победителей")
else:
    print("Ничья")
