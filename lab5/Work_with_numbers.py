from random import randint
from TintNumbers import TIntNumber2, TIntNumber16


def GenerateRandomBinNumbers(m, up, down):
    BinaryArr = []
    for i in range(m):
        object = TIntNumber2(None)
        object.number = bin(randint(down, up))
        BinaryArr.append(object)
    return BinaryArr


def GenerateRandomHexNumbers(n, up, down):
    HexArr = []
    for i in range(n):
        object = TIntNumber16(None)
        object.number = hex(randint(down, up))
        HexArr.append(object)
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

