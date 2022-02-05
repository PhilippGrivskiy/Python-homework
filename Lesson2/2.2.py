l = input("Введите список элементов через пробел: ")
l = l.split(' ')
print(l)

i = 0
while i < len(l)-1:
    if i % 2 == 0:
        l[i], l[i+1] = l[i+1], l[i]
    i += 1

print(l)
