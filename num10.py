from random import randint

N = int(input("Введите количество монет: "))
orel = reshka = 0
for i in range(N):
    x = randint(0, 1)
    print(x)
    if x == 0:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(
        f"Количество орлов: {orel}, количество решек: {reshka}. Переверните {orel} монет(-ы) с орла на решку."
    )
elif orel == reshka:
    print(
        f"Количество орлов: {orel}, количество решек: {reshka}. Количество орлов и решек одинаково, ничего переворачивать не нужно."
    )
else:
    print(
        f"Количество орлов: {orel}, количество решек: {reshka}. Переверните {reshka} монет(-ы) с решки на орла."
    )
