n = int(input("Введите количество арбузов "))
maxi = 0
mini = 100
for i in range(n):
    m = int(input("Введите вес арбуза "))
    if m > maxi:
        maxi = m
    if m < mini:
        mini = m
print(f"Минимальный вес арбуза: {mini}, максимальный вес арбуза: {maxi}")