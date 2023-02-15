# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума
# Ввод: мин = 7, макс = 10, список =[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def get_indexes_range(min_element, max_element, list_input):
    list_result = list()
    for i in range (len(list_input)):
        if min_element <= list_input[i] <= max_element:
            list_result.append(i)
    return list_result

min_element = int(input("Введите минимальное число диапазона: "))
max_element = int(input("Введите максимальное число диапазона: ")) 

print('Введите массив в строку: ')
list_input = list(map(int, input().split())) 
# list_input =[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

if max_element < min_element:
    print("Максимальный элемент не должен быть меньше минимального!")
else:
    print(f"Список индексов элементов массива между числами {min_element} и {max_element} включительно следующий: {get_indexes_range(min_element, max_element, list_input)}")
