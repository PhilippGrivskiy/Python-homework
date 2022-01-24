my_list = [9, 6, 5, 3, 2]
b = int(input("Введите число: "))
for index, e in enumerate(my_list):
    if b >= e:
        my_list.insert(index, b)
        break
else:
    my_list.append(b)
print(my_list)