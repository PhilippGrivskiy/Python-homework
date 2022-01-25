def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=False)
    return sum(my_list[1:])


print(my_func(100, 20, 50))