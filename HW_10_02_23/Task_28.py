# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4
def get_sum(a, b):
    if a < 1 and b < 1:
        return 0
    if a == 0 and b > 0:
        return b
    if a > 0 and b == 0:
        return a
    return get_sum(a - 1, b - 1) + 1 + 1

a = int(input("Enter first not negative number: "))
b = int(input("Enter second not negative number: ")) 

if a < 0 or b < 0:
    print("You should enter not negative numbers only!")
else:
    print(f"The sum of numbers {a} and {b} is equal to {get_sum(a, b)}")
