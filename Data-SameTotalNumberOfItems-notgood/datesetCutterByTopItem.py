filename = ''
mapingfile = ''
numberfile = ''

import os
print('please enter the filename (without suffix such as .csv)')
while True:
    pureFile = input()
    filename = pureFile + '.csv'
    abspath = os.path.dirname(os.path.abspath(filename))
    if os.path.exists(filename):
        mapingfile = pureFile + '-mapping.csv'
        numberfile = pureFile + '-number.csv'
        if os.path.exists(mapingfile) and os.path.exists(numberfile) :
            break;
        else :
            print('mapping file or numberfile is not exist')
    print('file is not exist')

while True:
    print('please enter the top item range (ie => 1,30,5)')
    stps = input().split(',')
    if len(stps) != 3 :
        continue
    else:
        start = int(stps[0])
        end = int(stps[1])
        step = int(stps[2])
        break
    
print(f'range = {start, end, step}')

import csv
def getTopItem(file, top) :
    with open(file, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
        data = data[0:top]
        topItemList = []
        for per in data :
            topItemList.append(str(per[0]))
        csvfile.close()
        print(topItemList)
        return topItemList

def getAllTransactions(file) :
    with open(file, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
        csvfile.close()
        return data

def filterTransaction(transcations, topItemList) :
    updatedTransactions = []
    for tran in transcations:
        newTran = []
        for item in tran :
            if item in topItemList:
                newTran.append(item)
        if len(newTran) > 0 :
            updatedTransactions.append(newTran)
    return updatedTransactions

def saveTofile(transactions, file, totalItem):
    print(file)
    with open(file, 'w+', newline='') as f:
        writer = csv.writer(f)
        i = 0
        tranLen = len(transactions) 
        totalNumOfItems = 0
        while i < tranLen:
            rowData = list(set(transactions[i]))
            rowData = sorted(rowData)
            totalNumOfItems += len(rowData)
            writer.writerow(rowData)
            if totalNumOfItems > totalItem:
                break
            i += 1
        f.close()


transactions = getAllTransactions(numberfile)
print(len(transactions))
for top in range(start, end, step) :
    topItemList = getTopItem(mapingfile, top)
    updatedTransactions = filterTransaction(transactions, topItemList)
    print(len(updatedTransactions))
    savedFilename = abspath + '/' + pureFile + '-number-TOP' + str(top) + '.csv'
    saveTofile(updatedTransactions, savedFilename, 10000)
    