#Попробовала двумя вариантами, т.к. первый вариант короткий, но при массиве, состоящем из разных чисел,
#считалось неверно порой. Во вторым мне кажется что наверчено слишком много, но то ли знаний не хватает,
#то ли туплю где-то.

N = int(input("Введите число (количество элементов массива): "))
x = int(
    input(
        "Введите число, к которому необходимо найти самый близкий элемент: "))

my_massiv = [i + 1 for i in range(N)]
min = abs(x - my_massiv[0])
index = 0
for i in range(1, N):
    count = abs(x - my_massiv[i])
    if count < min:
        min = count
        index = i

print(f"Полученный массив: {my_massiv}")
print(
    f"Выбрано число: {x}, наиболее близкое к нему число в массиве: {my_massiv[index]}."
)

'''
import random

N = int(input("Введите число (количество элементов массива): "))
x = int(
    input(
        "Введите число, к которому необходимо найти самый близкий элемент: "))

massiv = [random.randint(0, 20) for i in range(N)]
my_massiv = sorted(massiv)
i = 0
item = my_massiv[i]
result_number = 0
sec_number = 0
for item in my_massiv:
    if x > 0:
        if item - x <= 0:
            result_number = item
            i += 1
        else:
            if item - x > 0:
                sec_number = item
                break
    elif x < 0:
        result_number = my_massiv[0]
    else:
        "Что-то пошло не так"

print(f"Полученный массив: {my_massiv}")

if abs(result_number - x) < abs(sec_number - x):
    print(f"Ближайшее число к {x} в массиве: {result_number}")
elif abs(result_number - x) == abs(sec_number - x):
    print(f"Ближайшие числа к {x} в массиве: {result_number} и {sec_number}")
else:
    print(f"Ближайшее число к {x} в массиве: {sec_number}")
'''
