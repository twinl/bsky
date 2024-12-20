#!/usr/bin/python3 -W all
"""
    tscore-test.py: tests for tscore.py
    usage: tscore-test.py
    20171124 erikt(at)xs4all.nl
"""

import io
import re
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, 'scripts')
from tscore import computeTscore
from tscore import readData
from tscore import tscore
from tscore import writeData

DATA1 = { "totalFreq":3, "nbrOfWords":2, "wordFreqs":{"a":1, "b":2 } }
DATA2 = { "totalFreq":3, "nbrOfWords":2, "wordFreqs":{"b":1, "c":2 } }
RESULTS = {'c': -1.1547005383792517, 'a': 0.7071067811865475, 'b': 0.5}

def compareDicts(dict1,dict2):
    for key in dict1:
        if not key in dict2: return(False)
        if dict2[key] != dict1[key]: return(False) 
    for key in dict2:
        if not key in dict1: return(False)
    return(True)

class myTest(unittest.TestCase):
    def testComputeTscore(self):
        results = computeTscore(DATA1,DATA2)
        self.assertTrue(compareDicts(results,RESULTS))

    def testReadData(self): pass
    
    def testTscore(self): pass

    def testWriteData(self): pass
         
if __name__ == '__main__':
    unittest.main()
