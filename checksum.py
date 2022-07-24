# calculates the checksum for a UDP packet
def calcChecksum(data):
    checksum = bin(0)
    for i in range(0, int(len(data) / 32)):
        word = int(data[32 * i:32 * i + 32], 2)
        checksum = bin(int(checksum, 2) + word)
        if len(str(checksum)) > 34:
            checksum = "0b" + checksum[3:]
    return checksum


# method for calling the checksum method
def getChecksum(data):
    data = bin(int(data, 16))
    return list(str(calcChecksum(data))[2:])


# takes a 2 character string and a binary value and XORs them
def changeByte(byte, change):
    result = bin(int(byte, 2) ^ int(change, 2))
    return result


# changes input data until the desired checksum is reached
def changeCheck(targetCheckSum, data):
    currentChecksum = calcChecksum(data)
    difference = bin(targetCheckSum ^ int(currentChecksum, 2))
    while difference != bin(0):
        difference = bin(abs(int(difference, 2)))
        currentBit = difference[::-1].find("1")
        change = bin(2 ** currentBit)
        position = (int(len(data) / 32 - 5) * 32)
        word = data[position:position + 32]
        newWord = changeByte(word, change)
        newWord = "0" * (34 - len(newWord)) + newWord[2:]
        data = data[0:position] + newWord + data[position + 32:]
        currentChecksum = calcChecksum(data)
        difference = bin(targetCheckSum ^ int(currentChecksum, 2))
    return data


# takes in hidden data, udp data and index
def createPacket(hiddenData, index, data):
    hiddenData = bin(int(hiddenData, 16))
    data = bin(int(data, 16))
    checksum = index * (2 ** 16) + int(hiddenData, 2)
    print(hex(checksum), "2")
    return changeCheck(checksum, data)


# function for calling createPacket externally
def getPacket(hiddenData, index, data):
    return hex(int(createPacket(hiddenData, index, data), 2))[2:]
