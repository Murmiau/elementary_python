import random

N = int(input("Введите число (количество элементов массива): "))
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

massiv = [random.randint(0, 10) for i in range(N)]
my_index = []
i = 0

while i < N:
    if massiv[i] >= A and massiv[i] <= B:
        number = i
        my_index.append(number)
        i += 1
    else:
        i += 1

print(f"Полученный массив: {massiv}")
print(
    f"Выбрали для выводы индексов отрезок от: {A} до {B} включительно, индексы элементов в этом отрезке: {my_index}."
)
