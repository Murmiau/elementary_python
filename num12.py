import math

S = int(input("Загадайте два числа, введите их сумму: "))
P = int(input("Введите произведение этих двух чисел: "))
Discr = int(S**2 - 4 * P)

if Discr > 0:
    X = float((S + math.sqrt(Discr)) / 2)
    Y = float((S - math.sqrt(Discr)) / 2)
    print(f"Загаданные числа: {X} и {Y}")
elif Discr == 0:
    C = float(S // 2)
    print(f"Загаданы равные числа: {C} и {C}")
else:
    print("Решения нет")
