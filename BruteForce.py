import csv
import time
from itertools import combinations
import sys

def getDataFromFile(filename):
    with open(filename, newline='') as csvfile:
        data = [set(map(int, row)) for row in csv.reader(csvfile, skipinitialspace=True)]
    totalItems = sum(len(row) for row in data)
    print('BRUTE-FORCE')
    print(f'{filename} ==> rows = {len(data)}, total number of item = {totalItems}')
    return data, totalItems

def getAllPossibleItemsets(data):
    itemList = {item for transaction in data for item in transaction}
    if len(itemList) > 32:
        print('too large item list')
        exit()
    allSets = [tuple(combo) for i in range(1, len(itemList) + 1) for combo in combinations(itemList, i)]
    return allSets


def calculateSupportCount(itemset, data):
    itemset_set = set(itemset) ##########must transfer from here, do not merge code to below
    return sum(1 for transaction in data if itemset_set.issubset(transaction))

##############only support version > 3.8,   a little bit faster than below
def generateSupportList(data, allPossibleItemSets, minCount):
    return {itemset: support for itemset in allPossibleItemSets 
            if (support := calculateSupportCount(itemset, data)) >= minCount} 

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

def BruteForce(filename, minsupport, confidence=0):
    startTime = time.time()

    data, totalItems = getDataFromFile(filename)
    minCount = len(data) * minsupport
    itemsets = getAllPossibleItemsets(data)
    time1 = time.time()
    print(f'generate itemset time ==> {time1 - startTime}')
    frequentItemsets = generateSupportList(data, itemsets, minCount)

    print(f'frequent transaction ==> {frequentItemsets}')
    print(f'all process time ==> {time.time() - startTime}')
    print(f'number of transactions ==> {len(frequentItemsets)}')

    strongRelations = []
    if confidence > 0:
        strongRelations = generateConfidenceList(frequentItemsets, confidence)
        print(f'strong relation list => {strongRelations}')

    importantInfo = [filename, 'BRUTE FORCE', minsupport, len(data), totalItems, len(frequentItemsets),time.time() - startTime]
    return frequentItemsets, strongRelations, importantInfo

if __name__ == '__main__':
    BruteForce('Data/Market_Basket-number-TOP20.csv', 0.005)
