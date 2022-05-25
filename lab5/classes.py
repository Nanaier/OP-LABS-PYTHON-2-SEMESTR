from abc import ABC,  abstractmethod
from random import randint

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


def GenarateRandomBinNumbers(m, up, down):
    BinaryArr = [TIntNumber2(None)]*m
    for i in range(m):
        object = TIntNumber2(None)
        object.number = bin(randint(down, up))
        BinaryArr[i] = object
    return BinaryArr


def GenarateRandomHexNumbers(n, up, down):
    HexArr = [TIntNumber16(None)]*n
    for i in range(n):
        object = TIntNumber16(None)
        object.number = hex(randint(down, up))
        HexArr[i] = object
    return HexArr


def IncrementAndDecrement(BinaryArr, HexArr):
    print("Decremented binary numbers:")
    for i in range(len(BinaryArr)):
        BinaryArr[i] -= 1
        print(BinaryArr[i].number, end="  ")
    print()
    print("Incremented hex numbers:")
    for i in range(len(HexArr)):
        HexArr[i] += 1
        print(HexArr[i].number, end="  ")
    print()
    print("___________________________________")


def PrintArray(Arr):
    for i in range(len(Arr)):
        Arr[i].output()
    print("\n___________________________________\n")


def PrintArrayDec(Arr):
    for i in range(len(Arr)):
        print(Arr[i].TIntToDecimal(), end="  ")
    print()


def FindTheBiggestDecNumber(BinaryArr, HexArr):
    max = BinaryArr[0].TIntToDecimal()
    for i in range(len(BinaryArr)):
        if BinaryArr[i].TIntToDecimal() > max:
            max = BinaryArr[i].TIntToDecimal()
    for i in range(len(HexArr)):
        if HexArr[i].TIntToDecimal() > max:
            max = HexArr[i].TIntToDecimal()
    return max


def IndexesOfBiggest(BinaryArr, HexArr):
    numbers = []
    max = FindTheBiggestDecNumber(BinaryArr, HexArr)
    for i in range(len(BinaryArr)):
        if BinaryArr[i].TIntToDecimal() == max:
            numbers.append(BinaryArr[i].number)
            numbers.append("binary")
            break
    for i in range(len(HexArr)):
        if HexArr[i].TIntToDecimal() == max:
            numbers.append(HexArr[i].number)
            numbers.append("hex")
            break
    return numbers

