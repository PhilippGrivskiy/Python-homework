summ = 0

with open("File3") as file:
    lines = file.readlines()
    for line in lines:
        surname, salary = line.split()
        summ += int(salary)
        if int(salary) < 20000:
            print("Имеет оклад менее 20 тыс.: ", surname)

print("Средняя величина дохода сотрудников: ", summ/len(lines))