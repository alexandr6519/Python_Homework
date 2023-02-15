# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
n = int(input("Enter number of coins "))
minNumber = 0
numberCoinsWithBackSide = 0
for i in range(n):
    sideOfCoin = int(input(f"If coin number {i + 1} has backside, then enter '0',  else enter '1': " ))
    if sideOfCoin == 0:
        numberCoinsWithBackSide += 1
if numberCoinsWithBackSide < n - numberCoinsWithBackSide:
    minNumber = numberCoinsWithBackSide
else:
    minNumber = n - numberCoinsWithBackSide
print(f"If you want the all coins to lie on one side, you need to turn them at least {minNumber} times")