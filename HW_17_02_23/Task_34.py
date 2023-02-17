# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:пара-ра-рам рам-пам-папам па-ра-па-дам
#  Вывод: Парам пам-пам

def count_vowels(phrase):
    List_vowels = ["а", "е", "и", "о", "у", "ы", "э", "ю", "я"]
    count_result = 0
    for char in phrase:
        if char in List_vowels:
            count_result += 1
    return count_result

def is_rigth_poem(count_vowels, phrases):
    count_vowels_list = [count_vowels(phrase) for phrase in phrases]    
    for i in range(len(count_vowels_list) - 1):
        if count_vowels_list[i] != count_vowels_list[i + 1]:
            return False
    return True
print('Enter string: ')
list_poem = list(map(str, input().split(" ")))

if is_rigth_poem(lambda phrase: count_vowels(phrase), list_poem):
    print('Парам пам-пам')
else:
    print('Пам парам')
