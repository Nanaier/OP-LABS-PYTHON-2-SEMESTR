from abc import ABC, abstractmethod


class TIntNumber(ABC):
    def __init__(self, number, base):
        self.number = number
        self.base = base

    def TIntToDecimal(self):
        new_number = int(self.number, self.base)
        return new_number

    @abstractmethod
    def __iadd__(self, other):
        pass

    @abstractmethod
    def __isub__(self, other):
        pass

    def output(self):
        print(self.number, end="  ")


class TIntNumber2(TIntNumber):
    def __init__(self, number):
        super().__init__(number, 2)

    def __iadd__(self, other):
        new_number = self.TIntToDecimal()
        new_number += other
        self.number = bin(new_number)
        return self

    def __isub__(self, other):
        new_number = self.TIntToDecimal()
        new_number -= other
        self.number = bin(new_number)
        return self


class TIntNumber16(TIntNumber):
    def __init__(self, number):
        super().__init__(number, 16)

    def __iadd__(self, other):
        new_number = self.TIntToDecimal()
        new_number += other
        self.number = hex(new_number)
        return self

    def __isub__(self, other):
        new_number = self.TIntToDecimal()
        new_number -= other
        self.number = hex(new_number)
        return self
