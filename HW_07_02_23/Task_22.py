# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Введите количество чисел первого набора: "))
list_input_1 = list(map(int, input(f'Введите {n} натуральных чисел первого набора: ').split(' ')))
m = int(input("Введите количество чисел второго набора: "))
list_input_2 = list(map(int, input(f'Введите {m} натуральных чисел второго набора: ').split(' ')))

if n != len(list_input_1) or m != len(list_input_2):
    print("Вы ввели неверное количество чисел")
else:
    set_result = set(list_input_1).intersection(set(list_input_2))
    list_result = list(set_result)
    for i in range(len(list_result)):
        for j in range(i, len(list_result) - 1):
            if list_result[j + 1] < list_result[i]:
                (list_result[j + 1], list_result[i]) = (list_result[i], list_result[j + 1])
    print(f"Набор чисел {list_result} встречается в обоих наборах {list_input_1} и {list_input_2}!")
