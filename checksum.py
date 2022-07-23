import random


# calculates the checksum for a UDP packet
def calcChecksum(data):
    checksum = bin(0)
    for i in range(0, int(len(data) / 32)):
        word = int(data[32 * i:32 * i + 32], 2)
        print(word, "W")
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
    difference = bin(targetCheckSum ^ int(currentSum, 16))
    count = 0
    while difference != bin(0):
        count += 1
        difference = bin(abs(int(difference, 2)))

        currentBit = difference[::-1].find("1")

        change = bin(2**currentBit)

        random = int(ran.randint(0, int(len(data) / 32) * 32))
        word = data[random:random + 32]
        newWord = changeByte(word, change)
        data = data[0:random] + newWord + data[random + 32:]
        currentSum = calcChecksum(data)
        newdiffrence = bin(targetCheckSum ^ int(currentSum, 2))
        difference = newdiffrence
    return data


def createpacket(data, index, fileData):
    index = (index)
    checksum = index * (2**16) + int(data, 16)
    print(checksum, "2")
    return changeCheck(checksum, fileData)


ran = random.Random()
ran.seed(3)
data = '10000000000000000000000000000001110000000000000000000000000000011000000000000000000000000000000111000000000000000000000000000001'
print(calcChecksum(data), "1")
newData = createpacket('1234', 1, data)
print(newData, "3")
print(calcChecksum(data), "4")