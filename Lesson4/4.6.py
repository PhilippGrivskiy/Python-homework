from itertools import count, cycle
import sys

start_from = 10
iterable = "ABCDEF"
iterations_count = 0

def integer_generator(start_from):
    for el in count(start_from):
        if el > start_from+10:
            break
        yield el

for el in integer_generator(15):
    print(el)

print()

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break