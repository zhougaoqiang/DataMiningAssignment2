import csv
import os

# filename = 'database1.txt'
# newFilename = 'database1-new.txt'
# mapingFile = 'database1-maping.txt'
filename = ""
newFilename = ""
mapingFile = ""

while True :
    print('Input filename please')
    filename = input()
    if os.path.exists(filename):
        abspath = os.path.abspath(filename)
        path = os.path.dirname(abspath)
        pureFilename = os.path.basename(abspath).split('.')
        if (len(pureFilename) > 1):
            prefix = pureFilename[0]
            print(prefix)
            suffix = pureFilename[1:]
            strSuf = ''
            for str in suffix :
                strSuf = strSuf + str
            print(strSuf)
            newFilename = path + '/' + prefix + '-number.' + strSuf
            mapingFile = path + '/' + prefix + '-mapping.' + strSuf
        else :
            newFilename = path + '/' + pureFilename + '-number'
            mappingFile = path + '/' + pureFilename + '-mapping'
        break
    else:
        print("file is not exist, re-enter please!")


def getDataFromFile(filename) :
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
    print(len(data))
    csvfile.close()
    return data

data = getDataFromFile(filename)
itemDict = {}
itemCountDict = {}
index = 1000
tranLen = len(data)
i = 0
newData = []
for i in range(len(data)) :
    newRow = []
    for j in range (len(data[i])) :
        if (len(data[i][j]) == 0) : ## must filter empty options
            continue
        retIndex = itemDict.get(data[i][j], 0)
        if (retIndex == 0) :
            index += 1
            itemDict[data[i][j]] = index
            newRow.append(index)
            itemCountDict[data[i][j]] = 1
        else:
            newRow.append(retIndex)
            itemCountDict[data[i][j]] = itemCountDict[data[i][j]] + 1
    newData.append(newRow)
# print(itemDict)
# print(itemCountDict)
# print(newData)

itemListDict = []
totalItemCount = 0
itemCountList = []
for key, index in itemDict.items() :
    itemCount = itemCountDict.get(key)
    itemListDict.append([index, key, itemCount])
    itemCountList.append(itemCount)
    totalItemCount += itemCount

datelen = len(itemCountList)
#bubble sort
for j in range (datelen-1):
    count = 0
    for i in range (0, datelen-1-j) :
        if itemCountList[i] < itemCountList[i + 1] :
            itemCountList[i], itemCountList[i + 1] = itemCountList [i + 1], itemCountList[i]
            itemListDict[i], itemListDict[i + 1] = itemListDict [i + 1], itemListDict[i]
            count += 1
    if count == 0 :
        break;
 
itemListDict.append(["##########","total number of items in dataset => ", totalItemCount])

def writeTofile(data, filename) :
    print(filename)
    with open(filename, 'w+', newline='') as f:
        writer = csv.writer(f)
        i = 0
        tranLen = len(data)
        while i < tranLen:
            rowData = data[i]
            writer.writerow(rowData)
            i += 1
        f.close()
        
writeTofile(newData, newFilename)
writeTofile(itemListDict, mapingFile)
