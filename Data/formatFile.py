import os

filename = ""
formattedFilename = ""

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
            formattedFilename = path + '/' + prefix + '-formatted.' + strSuf
        else :
            formattedFilename = path + '/' + pureFilename + '-formatted'
        break
    else:
        print("file is not exist, re-enter please!")

import pandas as pd

def getDatafromFile(filename):
    filedata = pd.read_csv(filename, skipinitialspace=True)
    # print(len(filedata))
    header = list(filedata)
    print('Below is header and first 5 row for reference')
    print(header)
    print(filedata[:5])
    return header, filedata
    
header, filedata = getDatafromFile(filename)

while True :
    print('do you want remove any column? enter column name, 9999 to stop')
    col = input()
    if (header.count(col) > 0 ) :
        filedata.drop(col, axis=1, inplace=True)
        header.remove(col)
    elif col == '9999':
        break
    else :
        print('no match column')
    
    print(header)
    print(filedata[:5])
    continue

idCol = 0
itemCol = 1
while True:
    print("please confirm the transaction id column")
    idCol = int(input())
    print("please confirm the transaction item column")
    itemCol = int(input())
    break

data = {}
print(f'id column [{idCol}], item column [{itemCol}]')
dataLen = len(filedata)
print(dataLen)
i = 0
while i < dataLen:
    transId = filedata.iloc[i, idCol]
    transItem = filedata.iloc[i, itemCol]
    print(transId, transItem)
    if transId in data :
        itemList = data.get(transId)
        itemList.append(transItem)
        data[transId] = itemList
    else :
        data[transId] = [transItem]
    i += 1
import csv
def writeTofile(data, filename) :
    print(filename)
    with open(filename, 'w+', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items() :
            writer.writerow(value)
        f.close()

writeTofile(data, formattedFilename)