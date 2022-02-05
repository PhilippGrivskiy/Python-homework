from functools import reduce

source_list = [el for el in range(100, 1001, 2)]
print(source_list)

print()

result = reduce(lambda x, y: x*y, source_list)
print(result)