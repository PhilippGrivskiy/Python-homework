my_func_pow = lambda x, y: x**y

def my_func(x: float, y: int) -> float:
    if y > 0:
        return
    elif y== 0:
        return 1
    elif x <= 0:
        return
    else:
        return 1/x*my_func(x, y+1)


result = my_func_pow(2, -3)
print(result)
result = my_func(2, -3)
print(result if result else "Неверные входные данные!")