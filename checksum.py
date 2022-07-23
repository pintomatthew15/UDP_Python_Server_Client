import random


# calculates the checksum for a UDP packet
def calcChecksum(data):
    checksum = bin(0)
    for i in range(0, int(len(data) / 32)):
        word = int(data[32 * i:32 * i + 32], 2)
        checksum = bin(int(checksum, 2) + word)
        if (len(str(checksum)) > 34):
            checksum = "0b" + checksum[3:]
    return checksum

def getChecksum(data):
    return list(str(calcChecksum(data))[2:])

# takes a 2 character string and a binary value and XORs them
def changeByte(byte, change):
    result = bin(int(byte, 2) ^ int(change, 2))
    return result


# changes input data until the desired checksum is reached
def changeCheck(targetCheckSum, data):
    currentSum = calcChecksum(data)
    print(bin(targetCheckSum))
    print(bin(int(currentSum, 2)))
    difference = bin(targetCheckSum ^ int(currentSum, 2))
    count = 0
    while difference != bin(0):
        count += 1
        difference = bin(abs(int(difference, 2)))

        currentBit = difference[::-1].find("1")

        change = bin(2**currentBit)

        random = (int(ran.randint(0, int(len(data) / 32)))-1)*32
        word = data[random:random + 32]
        newWord = changeByte(word, change)
        newWord = "0" * (34 - len(newWord)) + newWord[2:]
        data = data[0:random] + newWord + data[random + 32:]
        currentSum = calcChecksum(data)
        difference = bin(targetCheckSum ^ int(currentSum, 2))
        print(bin(targetCheckSum), "T")
        print(bin(int(currentSum, 2)))
    return data


def createpacket(hiddenData, index, data):
    checksum = index * (2**16) + int(hiddenData, 16)
    print(checksum, "2")
    return changeCheck(checksum, data)

def stringToBin(hex):
    return bin(int(hex, 16))

ran = random.Random()
ran.seed(3)
d