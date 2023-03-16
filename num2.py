number = int(input("Введите трехзначное число: "))
summ = number // 100 + (number // 10) % 10 + number % 10
print(summ)
