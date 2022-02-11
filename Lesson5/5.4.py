translate_dict = {"One": "Один",
                  "Two": "Два",
                  "Three": "Три",
                  "Four": "Четыре",
                  "Five": "Пять",
                  "Six": "Шесть",
                  "Seven": "Семь"}

with open("File4") as file_read, open("File4_1", "w") as file_write:
    for line in file_read.readlines():
        text_number, number = line.rstrip().split(' - ')
        file_write.write(f'{translate_dict[text_number]} - {number}\n')