# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество чисел "))
list_input = list(map(int, input(f'Введите {n} натуральных чисел: ').split(' ')))
if len(list_input) == n:    
    x = int(input("Введите натуральное число "))
    result_element = list_input[0]
    min_dif = abs(x - result_element)
    for element in list_input[1:]:
        if abs(x - element) < min_dif:
            min_dif = abs(x - element)
            result_element = element
    print(f"Число {result_element} является самым близким по величине к числу {x} в массиве {list_input}!")
else:
    print("Вы ввели неверное количество чисел")