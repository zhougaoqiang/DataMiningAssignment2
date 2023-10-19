import csv
from itertools import combinations

#check support
def getDataFromFile(filename) :
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
    totalTrans = len(data)
    count = 0
    newData = []
    for row in data :
        newData.append([int(s) for s in row])
        count += len(row)
    print('APRIORI')
    print(f'{filename} ==> rows = {totalTrans}, total number of item = {count}')
    return newData, totalTrans, count

def getK1Itemset(data, supportCount) :
    itemDict = {}
    itemList = []
    for tran in data :
        for item in tran :
            if not [item] in itemList :
                itemList.append([item])

    for item in itemList :
        count = 0
        for trans in data :
            if item[0] in trans :
                count += 1
        if count >= supportCount:
            itemDict[tuple(item)] = count
        else:
            itemList.remove(item)
    return itemList, itemDict

def generateNextItemsetList(previousItemsetList, k) :
    nextItemsetList = []
    lenLk = len(previousItemsetList)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = sorted(previousItemsetList[i])[: k - 2]
            L2 = sorted(previousItemsetList[j])[: k - 2]
            if L1 == L2:   # ensure only last value is different, so unit len of value will add 1 only
                rtn = set(previousItemsetList[i])
                for item in previousItemsetList[j] :
                    rtn.add(item)
                nextItemsetList.append(list(rtn))
    return nextItemsetList
    

def getKnItemsetDict(data, knItemsetList, supportCount) :
    itemDict = {}
    for itemset in knItemsetList:    ########
        count = 0
        for transaction in data :    ########  rows
            if all(item in transaction for item in itemset):    #########items
                count += 1
        if count >= supportCount :
            itemDict[tuple(itemset)] = count
    # print(itemDict)
    return itemDict
                

###################################################
# check confidence
def sortItemsetToMultilevels(itemSupportDict) :
    keys = list(itemSupportDict.keys())
    # print(f'keys => {keys}')
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

from itertools import combinations
import time
def Apriori(filename, support, confidence = 0 ) :
    data, totalTrans, totalItems = getDataFromFile(filename)
    allItemset = {}
    supportCount = totalTrans * support
    # print(f'supportCount = {supportCount}')
    startTime = time.time()
    knItemsetList, k1ItemDict= getK1Itemset(data, supportCount)
    allItemset.update(k1ItemDict)
    itemsetLen = len(knItemsetList)
    duration = time.time() - startTime
    print(f'get all process time ==> {duration}')
    # print(k1ItemList)
    k = 2
    while itemsetLen > 1 :
        knItemsetList = generateNextItemsetList(knItemsetList, k)
        knItemDict = getKnItemsetDict(data, knItemsetList,supportCount)
        allItemset.update(knItemDict)
        itemsetLen = len(knItemDict)
        k += 1

    duration = time.time() - startTime
    print(f'get all process time ==> {duration}')
    strongRelationList = []
    if confidence > 0 :
        strongRelationList = generateConfidenceList(allItemset, confidence)
        print(f'strong relation list => {strongRelationList}')
    
    importantInfo = [filename, 'APRIORI', support, totalTrans, totalItems, duration]
    return allItemset, strongRelationList, importantInfo

if __name__ == '__main__':
    Apriori('Market_Basket-number-TOP16.csv', 0.005)
# else:
    # print('IMPORT APRIORI')
