word = str(input("Введите слово: "))

my_dict = dict({
    1: ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И',
        'Н', 'О', 'Р', 'С', 'Т'),
    2: ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'),
    3: ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'),
    4: ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'),
    5: ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч'),
    8: ('J', 'X', 'Ш', 'Э', 'Ю'),
    10: ('Q', 'Z', 'Ф', 'Щ', 'Ъ')
})

if word.isalpha() == True:

    def using_dict(dictionary, words):
        summ_letter = 0
        for key, value in dictionary.items():
            for letter in words.upper():
                if letter in value:
                    summ_letter += key
        print(summ_letter)

    using_dict(my_dict, word)
else:
    print("Ошибка, неверный ввод, нужно ввести слово!")
