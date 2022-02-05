revenue = int(input("Выручка фирмы: "))
costs = int(input("Издержки фирмы: "))

profit = revenue-costs

if profit > 0:
	print (f"Рентабельность капитала равна {profit/revenue * 100:.0f}%")
elif profit < 0:
	print ("Фирма работает в убыток")
else:
	print("У фирмы нулевая прибыль")

input("")