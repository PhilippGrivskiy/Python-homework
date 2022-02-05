def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Нельзя делить на ноль!"
    except TypeError:
        return "Неверные данные"


print(division(5, 20))
print(division(20, 5))
print(division(10, 0))
print(division("50", 100))