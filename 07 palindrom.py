word = str(input())
word = word.lower()
b = word[::-1]
if word == b:
    print("ПАЛИНДРОМ")
if word != b:
    print("НЕТ УЖ")
