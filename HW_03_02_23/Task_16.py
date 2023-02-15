# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input("Введите количество чисел "))
list_input = list(map(int, input(f'Введите {n} натуральных чисел: ').split(' ')))
if len(list_input) == n:
    count = 0
    x = int(input("Введите натуральное число "))
    for element in list_input:
        if element == x:
            count += 1
    word_times = "раз"
    if (count > 1 and count < 5) or (count > 20 and count % 10 > 1 and count % 10 < 5 ):
        word_times = "раза"
    print(f"Число {x} встречается в массиве {list_input} {count} {word_times}!")
else:
    print("Вы ввели неверное количество чисел")