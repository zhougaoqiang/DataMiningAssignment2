import Apriori
import BruteForce

filenameListForBF = [
            'Data/Bakery-formatted-number-TOP10.csv',
            'Data/Bakery-formatted-number-TOP20.csv',
            'Data/Groceries-formatted-number-TOP10.csv',
            'Data/Groceries-formatted-number-TOP20.csv',
            'Data/Market_Basket-number-TOP10.csv',
            'Data/Market_Basket-number-TOP20.csv',
            'Data/Online_Retail-formatted-code-number-TOP10.csv',
            'Data/Online_Retail-formatted-code-number-TOP20.csv',
            'Data/RetailScanner-formatted-category-number-TOP10.csv',
            'Data/RetailScanner-formatted-category-number-TOP20.csv',
            'Data/TVShows-number-TOP10.csv',
            'Data/TVShows-number-TOP20.csv'
           ]

filenameListForApriori = [
            'Data/Bakery-formatted-number-TOP10.csv',
            'Data/Bakery-formatted-number-TOP20.csv',
            'Data/Bakery-formatted-number-TOP30.csv',
            'Data/Bakery-formatted-number-TOP40.csv',
            'Data/Groceries-formatted-number-TOP10.csv',
            'Data/Groceries-formatted-number-TOP20.csv',
            'Data/Groceries-formatted-number-TOP30.csv',
            'Data/Groceries-formatted-number-TOP40.csv',
            'Data/Market_Basket-number-TOP10.csv',
            'Data/Market_Basket-number-TOP20.csv',
            'Data/Market_Basket-number-TOP30.csv',
            'Data/Market_Basket-number-TOP40.csv',
            'Data/Online_Retail-formatted-code-number-TOP10.csv',
            'Data/Online_Retail-formatted-code-number-TOP20.csv',
            'Data/Online_Retail-formatted-code-number-TOP30.csv',
            'Data/Online_Retail-formatted-code-number-TOP40.csv',
            'Data/RetailScanner-formatted-category-number-TOP10.csv',
            'Data/RetailScanner-formatted-category-number-TOP20.csv',
            'Data/RetailScanner-formatted-category-number-TOP30.csv',
            'Data/RetailScanner-formatted-category-number-TOP40.csv',
            'Data/TVShows-number-TOP10.csv',
            'Data/TVShows-number-TOP20.csv',
            'Data/TVShows-number-TOP30.csv',
            'Data/TVShows-number-TOP40.csv'
           ]


supportList = [0.01, 0.05]

information = [["filename", "type", "min support", "trans", "items", "time"]]

for filename in filenameListForApriori :
    for support in supportList :
        a,b,c = Apriori.Apriori(filename, support, confidence=0.5)
        information.append(c)
        
for filename in filenameListForBF :
    for support in supportList :
        d,e,f = BruteForce.BruteForce(filename, support,confidence=0.5)
        information.append(f)

print(information)
import csv
def writeTofile(data, filename) :
    print(filename)
    with open(filename, 'w+', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
        f.close()

writeTofile(information, 'TestResult-R1.csv')