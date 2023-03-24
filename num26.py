A = int(input("Введите число A: "))
B = int(input("Введите число B: "))


def exponentiation(A, B):
    if B == 0:
        return 1
    if B > 0:
        return A * exponentiation(A, B - 1)
    if B < 0:
        return 1 / A * exponentiation(A, B + 1)


print(f"Число {A} возведенное в степень {B} = {exponentiation(A, B)}")
