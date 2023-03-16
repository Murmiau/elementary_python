number = int(input("Введите шестизначное число: "))
a = number // 100000
b = number // 10000 % 10
c = number // 1000 % 10
d = number // 100 % 10
e = number // 10 % 10
f = number % 10
if (a + b + c == d + e + f):
    print(f"да, т.к. {a} + {b} + {c} = {d} + {e} + {f}")
else:
    print(f"нет, т.к. {a} + {b} + {c} не равно {d} + {e} + {f}")
