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
        Checksum16bitElements.append(data[i:i + 2].encode('utf-8').hex())
    result = hex(0)
    for i in range(0, len(Checksum16bitElements)):
        result = addTwo(result, Checksum16bitElements[i])
    result = hex(int(result, 16) ^ 0xFFFF)
    return result


def splitUpIP(ip):
    numbers = ip.split(".")
    numbers1 = hex(int(numbers[0]) * 256 + int(numbers[1]))
    numbers2 = hex(int(numbers[2]) * 256 + int(numbers[3]))
    return [numbers1, numbers2]


def addTwo(x, y):
    hex_sum = lambda a, b: hex(int(a, 16) + int(b, 16))
    # print("ADDING:", x, y)
    result = hex_sum(x, y)
    if len(result) > 6:
        result = hex(int(result, 16) - int("0x10000", 16))
        result = hex_sum(result, hex(1))
    return result


data = "AA"


def changeCheck(targetCheckSum, destIp, destPort, sourceIp, sourcePort, data):
    currentSum = calcChecksum(destIp, destPort, sourceIp, sourcePort, data)
    diffrence = hex(targetCheckSum - int(currentSum, 16))
    print(diffrence)
    data = hex(int(data.encode('utf-8').hex(), 16) - int(diffrence, 16))
    data = chr(int(data[0:4], 16)) + chr(int("0x"+data[4:], 16))
    print(data)
    newSum = calcChecksum(destIp, destPort, sourceIp, sourcePort, data)
    print(newSum)


print(changeCheck(0x5eec, "127.0.0.1", 20001, "127.0.0.1", 5000, data))
