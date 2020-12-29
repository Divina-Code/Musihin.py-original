import time
list = []
x = True
while x == True:
    answer = input("Что ты хочешь? Добавить, удалить, прочитать. Если ничего напиши хватит.    ").lower()
    if answer == "добавить":
        product = input("Что ты хочешь добавить?")
        list.append(product)
        print("Надеюсь я тебе угодил")
        time.sleep(1)
    if answer == "удалить":
        delt = input("Что ты хочешь удалить?")
        list.pop(delt)
        print("Надеюсь я тебе угодил")
        time.sleep(1)
    if answer == "прочитать":
        print(list)
        print("Надеюсь я тебе угодил")
        time.sleep(1)
    if answer == "хватит":
        print("Хозяин барин")
        x = False
