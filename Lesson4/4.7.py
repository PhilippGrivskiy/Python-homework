from itertools import count
from math import factorial


def fact(n):
    for i in count(1):
      if i <= n:
          result = factorial(i)
          yield result
      else:
          break

for el in fact(10):
    print(el)