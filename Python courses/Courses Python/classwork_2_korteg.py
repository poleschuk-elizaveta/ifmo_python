A = ('a', 1, 17, -9)
B = ('b', 4, 38, 16)
C = ('c', 12, 7, 8)
listABC = [A, B, C]
listY = list()
for i in listABC:
    print "%s: %d, %d, %d"%(i[0], i[1], i[2], i[3])
    listY.append(i[2])
    maxNum=max(listY)
    print maxNum

