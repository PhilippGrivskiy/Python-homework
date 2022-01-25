def int_func(word):
    return word.capitalize()

input_string = input("Введите строку: ")
result_string_list = []
input_words = input_string.split()
for element in input_words:
    result_string_list.append(int_func(element))

print(" ".join(result_string_list))