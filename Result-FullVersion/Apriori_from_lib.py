from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd
import csv
def getDataFromFile(filename) :
    with open(filename, newline='') as csvfile:
        data = list(csv.reader(csvfile, skipinitialspace=True))
    newData = []
    totalLen = 0
    for row in data :
        newData.append(row)
        totalLen += len(row)
    return newData, totalLen


# print(frequentTrans)
# print(f'execute time {time.time() - startTime}')

# ar = association_rules(frequentTrans, min_threshold=0.5)
# print(ar)

def Apriori(filename, support, confidence=0):
    import time
    startTime = time.time()
    trans, totalItem = getDataFromFile(filename)
    te = TransactionEncoder()
    te_ary = te.fit(trans).transform(trans)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequentTrans = apriori(df, support)
    print(len(frequentTrans))
    execTime = time.time() - startTime
    print(f'execute time {execTime}')

    if confidence > 0:
        ar = association_rules(frequentTrans, min_threshold=0.5)
        
    importantInfo = [filename, 'APRIORI', support, len(trans), totalItem, execTime]
    return frequentTrans, ar, importantInfo

if __name__ == '__main__':
    Apriori('Data/RetailScanner-formatted-category-number-TOP30.csv', 0.005, 0.5)