N = int(input("Введите количество кустов: "))
berries_list = list()
for i in range(N):
    berries = int(input("Введите количество ягод на кусте: "))
    berries_list.append(berries)

berries_count = list()
for i in range(len(berries_list) - 1):
    berries_count.append(berries_list[i - 1] + berries_list[i] + berries_list[i + 1])
berries_count.append(berries_list[-2] + berries_list[-1] + berries_list[0])
print(max(berries_count))
