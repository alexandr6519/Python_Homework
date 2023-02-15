# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8
n = int(input("Enter natural number  "))
if n < 1:
     print("You entered not natural number!!!")
else:
     temp = 1
     k = 0     
     while temp <= n:
        print(temp)
        k += 1
        temp = 2 ** k
        
