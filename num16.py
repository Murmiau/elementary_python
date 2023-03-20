import random

N = int(input("Введите число (количество элементов массива): "))
x = int(input("Введите число, которое необходимо подсчитать в массиве: "))

massiv = [random.randint(0, 10) for i in range(N)]
count = 0

for item in massiv:
    if item == x:
        count += 1

print(f"Полученный массив: {massiv}")
print(f"Выбрали для подсчета число: {x}, оно встречается {count} раз.")
'''
N = int(input("Введите число (количество элементов массива): "))
x = int(input("Введите число, которое необходимо подсчитать в массиве: "))

massiv=[i+1 for i in range(N)]
count = 0
for item in massiv:
    if item == x:
        count += 1

print(f"Полученный массив: {massiv}")
print(f"Выбрали для подсчета число: {x}, оно встречается {count} раз.")
'''
