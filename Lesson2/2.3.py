try:
    number_of_month = int(input("Введите номер месяца в виде числа от 1 до 12:  "))
except:
    print("Неверный формат числа")

else:
    winter = [12, 1, 2]
    spring = [3 ,4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10 ,11]

    if number_of_month in winter:
        print("Зима")
    elif number_of_month in spring:
        print("Весна")
    elif number_of_month in summer:
        print("Лето")
    elif number_of_month in autumn:
        print("Осень")
    else:
        print("Время года не определено")

