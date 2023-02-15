# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
s = int(input("Peet! Enter sum of 2 natural numbers (each of them should be no more than 1000): "))
p = int(input("Peet! Enter product of this numbers: "))
i = 1
while i < s:
    if (i + 1) * (s - i - 1) == p:
        x = i + 1
        y = s - i - 1
        break
    i += 1
print(f"Peet! You thought numbers: {x} and {y}")