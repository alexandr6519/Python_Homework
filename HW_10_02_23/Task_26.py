# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def get_exponention(n, m):
    if m == 0:
        return 1
    return get_exponention(n, m - 1) * n

a = int(input("Enter number: "))
b = int(input("Enter positive number: "))
if b < 1:
    print("You entered not positive number!")
else:
    print(f"The result of raising number {a} to the power of {b} is equal to {get_exponention(a, b)}")
    