my_phrase = input(
    "Введите слово или фразу из нескольких слов (разделенных дефисами)")


def f(my_phrase):
    return sum(1 for i in my_phrase if i in "аеёиоуыэюя")


letters = my_phrase.lower().split()
x = f(letters[0])
if all([f(i) == x for i in letters]):
    print("Парам пам-пам")
else:
    print("Пам парам")
