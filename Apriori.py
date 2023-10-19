import csv
import time

def getDataFromFile(filename):
    with open(filename, newline='') as csvfile:
        data = [list(map(int, row)) for row in csv.reader(csvfile, skipinitialspace=True)]
    totalTrans = len(data)
    totalItems = sum(len(row) for row in data)
    print('APRIORI')
    print(f'{filename} ==> rows = {totalTrans}, total number of item = {totalItems}')
    return data, totalTrans, totalItems

def getK1Itemset(data, supportCount):
    itemCounter = {}
    for tran in data:
        for item in tran:
            if item in itemCounter:
                itemCounter[item] += 1
            else:
                itemCounter[item] = 1
    itemList = [[item] for item, count in itemCounter.items() if count >= supportCount]
    itemDict = {(item,): count for item, count in itemCounter.items() if count >= supportCount}
    return itemList, itemDict


def generateNextItemsetList(previousItemsetList, k):
    nextItemsetList = []
    lenLk = len(previousItemsetList)
 
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = sorted(previousItemsetList[i])
            L2 = sorted(previousItemsetList[j])
            if L1[:k - 2] == L2[:k - 2]:
                L1.append(L2[k-2])
                rtn = L1
                nextItemsetList.append(rtn)
    return nextItemsetList

def getKnItemsetDict(data, knItemsetList, supportCount):
    itemDict = {}
    newKnItemsetList = []
    for itemset in knItemsetList:
        itemset_set = set(itemset)
        count = sum(1 for transaction in data if itemset_set.issubset(transaction))
        if count >= supportCount:
            itemDict[tuple(itemset)] = count
            newKnItemsetList.append(itemset)
    return itemDict, newKnItemsetList

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

def Apriori(filename, support, confidence=0):
    data, totalTrans, totalItems = getDataFromFile(filename)
    allItemset = {}
    supportCount = totalTrans * support
    
    startTime = time.time()
    knItemsetList, k1ItemDict = getK1Itemset(data, supportCount)
    allItemset.update(k1ItemDict)
    itemsetLen = len(knItemsetList)
    duration = time.time() - startTime
    print(f'get k1 process time ==> {duration}')
    k = 2
    while itemsetLen > 1:
        knItemsetList = generateNextItemsetList(knItemsetList, k)
        knItemDict, knItemsetList = getKnItemsetDict(data, knItemsetList, supportCount)
        allItemset.update(knItemDict)
        itemsetLen = len(knItemDict)
        k += 1

    duration = time.time() - startTime
    print(f'get all process time ==> {duration}')
    print(f'get frequent trans ==> {allItemset}')
    print(f'length of frequent trans ==> {len(allItemset)}')
    strongRelationList = []
    if confidence > 0:
        strongRelationList = generateConfidenceList(allItemset, confidence)
        print(f'strong relation list => {strongRelationList}')
        print(f'length => {len(strongRelationList)}')
    
    importantInfo = [filename, 'APRIORI', support, totalTrans, totalItems, len(allItemset), duration]
    return allItemset, strongRelationList, importantInfo

if __name__ == '__main__':
    Apriori('Data/RetailScanner-formatted-category-number-TOP30.csv', 0.005)
