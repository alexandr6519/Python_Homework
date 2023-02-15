# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
s = int(input("Peet! Enter sum of 2 natural numbers (each of them should be no more than 1000): "))
p = int(input("Peet! Enter product of this numbers: "))
if s < 1 or p < 1 or s > 2000 or p > 1000000:
    print("Peet! You entered incorrect numbers: ")
else:
    i = 1
    while i < s:
        if (i + 1) * (s - i - 1) == p:
            x = i + 1
            y = s - i - 1
            break
        i += 1
    print(f"Peet! You thought numbers: {x} and {y}")
        
