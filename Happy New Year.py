import time
import random
from random import randint
number = int(input())
while number != 20 :
    y = "    " * randint(1,12)
    print(y," *X  *X  *  *  " * number)
    print(y," *X *X* *  " * number)
    time.sleep(1)
    number += 1
time.sleep(1)
print("Вот вам снегопад")
time.sleep(1)
print("С новым годом:)")




