from classes import *

m = int(input("Enter the amount of binary numbers m: "))

down = int(input("Enter down limit for generated numbers: "))
up = int(input("Enter up limit for generated numbers: "))

BinaryArr = GenarateRandomBinNumbers(m, up, down)
print("\nRandomly generated binary numbers:")
PrintArray(BinaryArr)

n = int(input("Enter the amount of hex numbers m: "))

down = int(input("Enter down limit for generated numbers: "))
up = int(input("Enter up limit for generated numbers: "))

HexArr = GenarateRandomHexNumbers(n, up, down)
print("\nRandomly generated hex numbers:")
PrintArray(HexArr)

print("Those numbers in decimal system:\n")

print("Binary array into decimal:")
PrintArrayDec(BinaryArr)
print("Hex array into decimal:")
PrintArrayDec(HexArr)
print("___________________________________")

print("Incremented and Decremented numbers:\n")
IncrementAndDecrement(BinaryArr, HexArr)

print("Those numbers in decimal system:\n")

print("Binary array into decimal:")
PrintArrayDec(BinaryArr)
print("Hex array into decimal:")
PrintArrayDec(HexArr)
print("___________________________________")

print("The biggest number in decimal system: ", FindTheBiggestDecNumber(BinaryArr, HexArr))

numbers = IndexesOfBiggest(BinaryArr, HexArr)
print("Searched number in its system/s:\n")

for i in range(0, len(numbers), 2):
    print(numbers[i], "is the biggest number and it was written in", numbers[i+1], "system")

