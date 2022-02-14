class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError("num should be > 0")
            self.num = int(num)
        except TypeError:
            self.num = 1
            print("Check num value")
        except ValueError:
            print("Check num value")
            self.num = 1

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print("Subtraction is impossible")

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell_1 = Cell(12)
cell_2 = Cell(15)
print(cell_1.make_order(3))
print()
print(cell_2.make_order(7))
print()
cell_3 = cell_2*cell_1
print(cell_3.make_order(8))




















