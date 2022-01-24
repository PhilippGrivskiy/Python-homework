input_string = input("Введите строку из нескольких слов: ")
input_words = input_string.split()

i = 1
for word in input_words:
    print(i, word[:10])
    i += 1