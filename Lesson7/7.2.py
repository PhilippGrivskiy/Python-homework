from abc import ABC, abstractmethod

class Stuff(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def get_consumtion(self):
        pass

class Coat(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f"There is a new coat with size {self.param}")

    @property
    def get_consumtion(self):
        return round(self.param / 6.5 + 0.5, 2)

class Suit(Stuff):
    def __init__(self, param):
        super().__init__(param)
        print(f"There is a new suit with height {self.param}")

    @property
    def get_consumtion(self):
        return round(self.param * 2 + 0.3, 2)

my_coat = Coat(48)
print(f'Tissue consumption for my coat is: {my_coat.get_consumtion}')
my_suit = Suit(1.78)
print(f'Tissue consumption for my coat is: {my_suit.get_consumtion}')
print(f'The total issue consumption is: {my_coat.get_consumtion + my_suit.get_consumtion}')