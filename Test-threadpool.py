######parameters

'''    <<<VERY IMPORTANT>>>
Pre-condition for MultiProcessing Time Verification.
1. CPU hyper-threading should be disabled.
2. Number of multi-processing should not over REAL total CPU core count. Better number is number of core - 1
3. No other program running at the same time. 

Based on above pre-conditions with multiple tests, 
I observed consistent runtime performance for identical datasets under the same parameters. 
This was consistent across multiple tests with equivalent core performance.
Given this consistency, I've chosen to utilize multi-process mode to enhance data processing speed.
'''


filenameListForBF = [
            'Data/Bakery-formatted-number-TOP10.csv',
            'Data/Bakery-formatted-number-TOP20.csv',
            # 'Data/Groceries-formatted-number-TOP10.csv',
            # 'Data/Groceries-formatted-number-TOP20.csv',
            'Data/Market_Basket-number-TOP10.csv',
            'Data/Market_Basket-number-TOP20.csv',
            'Data/Online_Retail-formatted-code-number-TOP10.csv',
            'Data/Online_Retail-formatted-code-number-TOP20.csv',
            'Data/RetailScanner-formatted-category-number-TOP10.csv',
            'Data/RetailScanner-formatted-category-number-TOP20.csv',
            # 'Data/TVShows-number-TOP10.csv',
            # 'Data/TVShows-number-TOP20.csv'
           ]

filenameListForApriori = [
            'Data/Bakery-formatted-number-TOP10.csv',
            'Data/Bakery-formatted-number-TOP20.csv',
            'Data/Bakery-formatted-number-TOP30.csv',
            'Data/Bakery-formatted-number-TOP40.csv',
            # 'Data/Groceries-formatted-number-TOP10.csv',
            # 'Data/Groceries-formatted-number-TOP20.csv',
            # 'Data/Groceries-formatted-number-TOP30.csv',
            # 'Data/Groceries-formatted-number-TOP40.csv',
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
            # 'Data/TVShows-number-TOP10.csv',
            # 'Data/TVShows-number-TOP20.csv',
            # 'Data/TVShows-number-TOP30.csv',
            # 'Data/TVShows-number-TOP40.csv'
           ]


supportList = [0.01, 0.05]
information = [["filename", "type", "min support", "trans", "items", "len of frequentItemset","time"]]


###############################################
# import sys
# import os
# import time
# 
# time_str = time.strftime('%Y%m%d%H%M')
# log_file = "Output-" + time_str + ".log"
# class Logger(object):
    # def __init__(self, filename=log_file):
        # self.terminal = sys.stdout
        # self.log = open(filename, "a")
# 
    # def write(self, message):
        # self.terminal.write(message)
        # self.log.write(message)
# 
    # def flush(self):
        # pass
# 
# sys.stdout = Logger(log_file)
###############################################################

# main_script.py
from multiprocessing import get_context
import csv
# from RunThread import runInThread
from RunThread import runAprioriOnly
from RunThread import runBruteForceOnly
from RunThread import runAprioriFromLib

cpucores = 4 ########Should update for different computer

def main():
    with get_context('spawn').Pool(cpucores) as p:
        results = []
        for i in range(3) :  ####run multiple times to get average value
            for filename in filenameListForApriori:   #####run different support value for Apriori Support impact verification
                for support in supportList:
                    results.append(p.apply_async(runAprioriOnly, args=(filename, support)))
            for filename in filenameListForBF:  ###########BF will not be affectted by support
                    results.append(p.apply_async(runBruteForceOnly, args=(filename, supportList[0])))
        
        for filename in filenameListForApriori:   #####for result verfication only, run 1 time only
            for support in supportList:
                results.append(p.apply_async(runAprioriFromLib, args=(filename, support)))
        
        
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

    writeTofile(information, 'TestResult.csv')

if __name__ == '__main__':
    main()
