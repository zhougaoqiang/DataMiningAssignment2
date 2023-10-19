######parameters

'''
When hyper-threading is disabled, and without surpassing the total CPU core count, 
I observed consistent runtime performance for identical data sets under the same parameters. 
This was consistent across multiple tests with equivalent core performance.
Given this consistency, I've chosen to utilize multi-process mode to enhance data processing speed.
'''


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

# main_script.py
from multiprocessing import get_context
import csv
from RunThread import runInThread
from RunThread import runAprioriOnly
from RunThread import runBruteForceOnly

cpucores = 4
def main():
    with get_context('spawn').Pool(cpucores) as p:
        results = []
        for filename in filenameListForApriori:
            for support in supportList:
                results.append(p.apply_async(runAprioriOnly, args=(filename, support)))
        for filename in filenameListForBF:
            for support in supportList:
                results.append(p.apply_async(runBruteForceOnly, args=(filename, support)))

        p.close()
        p.join()
        for result in results:
            print(result.get())
            information.extend(result.get())

    print(information)
    def writeTofile(data, filename):
        print(filename)
        with open(filename, 'w+', newline='') as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)
            f.close()

    writeTofile(information, 'TestResult-ThreadPool-R1.csv')

if __name__ == '__main__':
    main()
