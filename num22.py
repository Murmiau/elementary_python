A = int(input("Введите число (количество элементов списка): "))
B = int(input("Введите число (количество элементов списка): "))

list_1 = []
for i in range(A):
    list_1.append(int(input("Введите число: ")))
print(f"Первый список: {list_1}")

list_2 = []
for j in range(B):
    list_2.append(int(input("Введите число: ")))
print(f"Второй список: {list_2}")

for j in list_2:
    list_1.append(j)

list_1.sort()

result_list = []
i = 0
for i in range(len(list_1)):
    for k in range(i + 1, len(list_1)):
        if list_1[i] == list_1[k]:
            result_list.append(list_1[i])
            i += 1
        else:
            i += 1

result_list = list(set(result_list))

print(f"Результат объединения списков и их сортировки: {result_list}")
