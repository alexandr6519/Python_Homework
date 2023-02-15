# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
n = int(input("Please, enter 3-digital number! "))
if n > 99 and n < 1000: 
    print('The sum of digitals of number {} is: {}'.format(n, n % 10 + n // 10 % 10 + n // 100 % 10)) 
else: 
    print("You entered incorrect number (not 3-digital)!")
    