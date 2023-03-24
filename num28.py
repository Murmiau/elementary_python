A = int(input("Введите число A: "))
B = int(input("Введите число B: "))


def summ(A, B):
    if A == 0:
        return B
    if B == 0:
        return A
    if B > 0:
        return 1 + summ(A, B - 1)
    if A > 0 and B < 0:
        return 1 + summ(A - 1, B)
    if A < 0 and B < 0:
        return -1 + summ(A + 1, B)


print(f"Сумма чисел {A} и {B} = {summ(A,B)}")
