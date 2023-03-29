A = int(input("Введите первое число прогрессии: "))
difference = int(input("Введите разность: "))
N = int(input("Введите количество элементов прогрессии: "))

i = 0
progression = []

for i in range(N):
    a = A + (difference * i)
    i += 1
    progression.append(a)

print(*progression, sep="\n")
