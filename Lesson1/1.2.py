sec = int(input("Введите количество секунд: "))

hours = sec // 3600
minutes = sec % 3600 // 60
sec = sec % 60 
print(f"{hours:02}:{minutes:02}:{sec:02}")

input("")