a = int(input("Результат спортсмена в 1й день: "))
b = int(input("Желаемая дистанция: "))

days = 1
while a < b:
	a *= 1.1
	days += 1

print(f"Спортсмен достигнет дистанции в {b} км за {days} дней")

input("")