import random
from random import Random
import time


# takes a 2 letter string and returns the hex value
def twoToHex(letters):
    letter1 = ord(letters[0])
    letter2 = ord(letters[1])
    total = hex(letter1 * 256 + letter2)
    return total


# calculates the checksum for a UDP packet
def calcChecksum(destIp, destPort, sourceIp, sourcePort, data):
    Checksum16bitElements = []
    Checksum16bitElements.append(splitUpIP(sourceIp)[0])
    Checksum16bitElements.append(splitUpIP(destIp)[1])
    Checksum16bitElements.append(splitUpIP(destIp)[0])
    Checksum16bitElements.append(splitUpIP(destIp)[1])
    Checksum16bitElements.append(hex(17))
    Checksum16bitElements.append(hex(8 + len(data)))
    Checksum16bitElements.append(hex(sourcePort))
    Checksum16bitElements.append(hex(destPort))
    Checksum16bitElements.append(hex(8 + len(data)))
    for i in range(0, int(len(data) / 2)):
        Checksum16bitElements.append(twoToHex(data[2 * i:2 * i + 2]))
    result = hex(0)
    for i in range(0, len(Checksum16bitElements)):
        result = addTwo(result, Checksum16bitElements[i])
    result = hex(int(result, 16) ^ 0xFFFF)
    return result


# takes an ip and returns the 16bit hex values
def splitUpIP(ip):
    numbers = ip.split(".")
    numbers1 = hex(int(numbers[0]) * 256 + int(numbers[1]))
    numbers2 = hex(int(numbers[2]) * 256 + int(numbers[3]))
    return [numbers1, numbers2]


# takes two hex values and adds them with LSB carry
def addTwo(x, y):
    hex_sum = lambda a, b: hex(int(a, 16) + int(b, 16))
    # print("ADDING:", x, y)
    result = hex_sum(x, y)
    if len(result) > 6:
        result = hex(int(result, 16) - int("0x10000", 16))
        result = hex_sum(result, hex(1))
    if len(result) > 6:
        print("WTFTHISSHOUDLNOTHAPPEN")
    return result


# takes a 2 character string and a binary value and XORs them
def changeString(twochar, diffrence, amount):
    binvals = bin(int(twoToHex(twochar), 16))
    while diffrence.find("1") != -1 and amount > 0:
        index = diffrence.find("1")
        diffrenceSaved = diffrence
        diffrence = diffrence[0:index] + "0" + diffrence[index + 1:]
        if diffrence.find("1") == -1:
            diffrence = diffrenceSaved
        amount -= 1
    result = bin(int(binvals, 2) ^ int(diffrence, 2))
    result = "0b" + (18 - len(result)) * "0" + result[2:]
    letter1 = chr(int(result[2:10], 2))
    letter2 = chr(int(result[10:19], 2))
    total = letter1 + letter2
    return total


# chages input data until the desired checksum is reached
def changeCheck(targetCheckSum, destIp, destPort, sourceIp, sourcePort, data):
    currentSum = calcChecksum(destIp, destPort, sourceIp, sourcePort, data)
    diffrence = hex(targetCheckSum ^ int(currentSum, 16))
    count = 0
    while diffrence != hex(0):
        count += 1
        diffrence = bin(int(diffrence, 16))
        if (diffrence[0] == "-"):
            diffrence = diffrence[1:]
        random = int(ran.randint(0, (len(data) - 2) * 2) / 2)
        letters = data[random:random + 2]
        newLetters = changeString(letters, diffrence, 3)
        data = data[0:random] + newLetters + data[random + 2:]
        currentSum = calcChecksum(destIp, destPort, sourceIp, sourcePort, data)
        newdiffrence = hex(targetCheckSum ^ int(currentSum, 16))
        diffrence = newdiffrence
    return data


data = ""
for i in range(0, 500):
    data += chr(random.randint(0, 255))
ran = Random()
ran.seed(3)
for i in range(0, 10):
    start_time = time.time()
    newdata = changeCheck(0x5eec, "127.0.0.1", 20001, "127.0.0.1", 5000, data)
    bins= bin(int(data.encode().hex(), 16) ^ int(newdata.encode().hex(), 16))
    print(bins.count("1")/len(bins))
    #print(newdata)
    print("--- %s seconds ---" % (time.time() - start_time))
