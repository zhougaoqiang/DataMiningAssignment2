import csv
from itertools import combinations

#check support
def getDataFromFile(filename) :
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
    newData = []
    count = 0
    for row in data :
        newData.append([int(s) for s in row])
        count += len(row)
    print('BRUTE-FORCE')
    print(f'{filename} ==> rows = {len(newData)}, total number of item = {count}')
    return newData, count

def getAllPossibleItemsets(data) :
    itemList = set()
    for transactions in data :
        for item in transactions :
            itemList.add(item) 
            
    itemLen = len(itemList)
    
    if (itemLen > 32) :
        print('too large item list')
        exit()
    itemSets = set()
    for i in range (1, itemLen + 1):
        combination = combinations(itemList, i)
        itemSets.update(list(combination))  #add all possible length i options to itemsets
    return itemSets

def calculateSupportCount(itemset, data) :
    count = 0
    # hasExistInData = False
    for transaction in data: # supports: fraction of transactions that contain bot X and Y
        if all(item in transaction for item in itemset) :
            count += 1
            # if hasExistInData == False : 
                # if all(item in itemset for item in transaction) :
                    # hasExistInData = True
    return count #, hasExistInData

#return support list which each itemset support >= min support count
def generateSupportList(data, allPossibleItemSets, minSupport) :
    itemSupportDict = {}
    dataLen = len(data)
    for itemset in allPossibleItemSets :
        supportCount = calculateSupportCount(itemset, data)
        if supportCount/dataLen >= minSupport: #not exists in data
            itemSupportDict[itemset] = supportCount
    return itemSupportDict


###################################################
# check confidence
def sortItemsetToMultilevels(itemSupportDict) :
    keys = list(itemSupportDict.keys())
    levelDict = {}
    for key in keys :
        itemLen = len(key)
        if itemLen in levelDict :
            level = levelDict.get(itemLen)
            level.append(key)
        else :
            levelDict[itemLen] = [key]
    return levelDict

def generateConfidenceList(itemSupportDict, minConfidence) :
    levelDict = sortItemsetToMultilevels(itemSupportDict)
    keys = sorted(levelDict.keys())
    # print("keys:")
    # print(keys)
    strongRelationList = []
    for i in range(len(keys) - 1) :
        key = keys[i]
        prevLevel = levelDict.get(key)
        nextLevel = levelDict.get(keys[i + 1])
        for preTran in prevLevel :
            preTranCount = itemSupportDict.get(preTran)
            for nextTran in nextLevel :
                if all(item in nextTran for item in preTran) :
                    nextTranCount = itemSupportDict.get(nextTran)
                    confidence = nextTranCount/preTranCount
                    # print(f'get confident {confidence}')
                    if (confidence >= minConfidence):
                        relationList = [preTran,preTranCount,nextTran,nextTranCount,confidence]
                        strongRelationList.append(relationList)
    return strongRelationList

import time
def BruteForce(filename, minsupport, confidence = 0) :
    startTime = time.time()
    data, totalItem = getDataFromFile(filename)
    itemsets = getAllPossibleItemsets(data)
    time1 = time.time()
    print(f'generate itemset time ==> {time1 - startTime}')
    frequentTransactions = generateSupportList(data, itemsets, minsupport)
    print(f'frequent transaction ==> {frequentTransactions}')
    duration = time.time() - startTime
    print(f'all process time ==> {duration}')
    print(f'number of transcations ==> {len(frequentTransactions)}')
    strongRelationList = []
    if confidence > 0 :
        strongRelationList = generateConfidenceList(frequentTransactions, confidence)
        print(f'strong relation list => {strongRelationList}')
    # importantInfo = {}
    # importantInfo['type'] = 'BRUTE FORCE'
    # importantInfo['minsupport'] = minsupport
    # importantInfo['filename'] = filename
    # importantInfo['number of transactions'] = len(data)
    # importantInfo['number of item in data'] = totalItem
    # importantInfo['processing time'] = duration
    importantInfo = [filename, 'BRUTE FORCE', minsupport, len(data), totalItem, duration]
    return frequentTransactions, strongRelationList, importantInfo

if __name__ == '__main__':
    BruteForce('Data/Groceries-formatted-number-TOP12.csv', 0.005)
# else:
    # print('IMPORT BRUTE FORCE')