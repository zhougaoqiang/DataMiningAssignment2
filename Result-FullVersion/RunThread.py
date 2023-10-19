# thread_functions.py
import Apriori
import BruteForce

def runInThread(filename, support):
    a, b, c = Apriori.Apriori(filename, support, confidence=0.5)
    d, e, f = BruteForce.BruteForce(filename, support, confidence=0.5)
    return [c, f]


def runAprioriOnly(filename, support) :
     a, b, c = Apriori.Apriori(filename, support, confidence=0.5)
     return [c]
 
def runBruteForceOnly(filename, support) :
     a, b, c = BruteForce.BruteForce(filename, support, confidence=0.5)
     return [c]

import Apriori_from_lib
def runAprioriFromLib(filename, support) :
     a,b,c = Apriori_from_lib.Apriori(filename, support, confidence=0.5)
     return [c]

import FPGrowth_from_lib
def runFPGrowthFromLib(filename, support) :
     a,b,c = FPGrowth_from_lib.FPGrowth(filename, support, confidence=0.5)
     return [c]