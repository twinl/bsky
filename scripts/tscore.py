#!/usr/bin/python3 -W all
"""
    tscore.py: compute t-scores for the vocabulary of two fasttext file labels
    usage: tscore.py label1 [label2] < file
    note: source: Church, Gale, Hanks & Hindle, 1991, page 9
    20171124 erikt(at)xs4all.nl
"""

import math
import sys

COMMAND = sys.argv[0]
USAGE = "usage: "+COMMAND+" label1 [label2]"

def readData(label1,label2):
    data1 = { "totalFreq":0, "nbrOfWords":0, "wordFreqs":{} }
    data2 = { "totalFreq":0, "nbrOfWords":0, "wordFreqs":{} }
    for line in sys.stdin:
        tokens = line.split()
        if tokens[0] == label1:
            for i in range(1,len(tokens)):
                data1["totalFreq"] += 1.0
                if tokens[i] in data1["wordFreqs"]: 
                    data1["wordFreqs"][tokens[i]] += 1.0
                else:
                    data1["wordFreqs"][tokens[i]] = 1.0
                    data1["nbrOfWords"] += 1.0
        if tokens[0] == label2 or \
           (label2 == "" and tokens[0] != label1):
            for i in range(1,len(tokens)):
                data2["totalFreq"] += 1.0
                if tokens[i] in data2["wordFreqs"]:
                    data2["wordFreqs"][tokens[i]] += 1.0
                else:    
                    data2["wordFreqs"][tokens[i]] = 1.0
                    data2["nbrOfWords"] += 1.0
    return(data1,data2)

def tscore(f1,f2,t1,t2,n1,n2):
    p1 = (f1+0.5)/(t1+n1/2.0)
    p2 = (f2+0.5)/(t2+n2/2.0)
    s1 = (f1+0.5)/math.pow(t1+n1/2.0,2.0)
    s2 = (f2+0.5)/math.pow(t2+n2/2.0,2.0)
    return((p1-p2)/math.sqrt(s1+s2))

def tscoreUniqueWords(f1,f2,n1,n2):
    p1 = (f1+0.5)/(n1+0.5)
    p2 = (f2+0.5)/(n2+0.5)
    s1 = (f1+0.5)/math.pow(n1+0.5,2.0)
    s2 = (f2+0.5)/math.pow(n2+0.5,2.0)
    return((p1-p2)/math.sqrt(s1+s2))

def computeTscore(data1,data2):
    tscores = {}
    t1 = data1["totalFreq"]
    t2 = data2["totalFreq"]
    n1 = data1["nbrOfWords"]
    n2 = data2["nbrOfWords"]
    for token in data1["wordFreqs"]:
        f1 = data1["wordFreqs"][token]
        if token in data2["wordFreqs"]: f2 = data2["wordFreqs"][token]
        else: f2 = 0.0
        tscores[token] = tscore(f1,f2,t1,t2,n1,n2)
    for token in data2["wordFreqs"]:
        if not token in data1["wordFreqs"]:
            f2 = data2["wordFreqs"][token]
            f1 = 0.0
            tscores[token] = tscore(f1,f2,t1,t2,n1,n2)
    return(tscores)

def computeTscoreUniqueWords(data1,data2):
    tscores = {}
    n1 = data1["maxCount"]
    n2 = data2["maxCount"]
    for token in data1["wordFreqs"]:
        f1 = data1["wordFreqs"][token]
        if token in data2["wordFreqs"]: f2 = data2["wordFreqs"][token]
        else: f2 = 0.0
        tscores[token] = tscoreUniqueWords(f1,f2,n1,n2)
    for token in data2["wordFreqs"]:
        if not token in data1["wordFreqs"]:
            f2 = data2["wordFreqs"][token]
            f1 = 0.0
            tscores[token] = tscoreUniqueWords(f1,f2,n1,n2)
    return(tscores)

def writeData(tscores,data1,data2):
    for token in sorted(tscores,key=tscores.get):
        if token in data1["wordFreqs"]: f1 = data1["wordFreqs"][token]
        else: f1 = 0.0
        if token in data2["wordFreqs"]: f2 = data2["wordFreqs"][token]
        else: f2 = 0.0
        print("{0:.3f} {1:5.0f} {2:5.0f} {3}".format(tscores[token],f1,f2,token))

def main(argv):
    argv.pop(0)
    if len(argv) == 2:
        label1,label2 = argv
    elif len(argv) == 1:
        label1 = argv[0]
        label2 = ""
    else:
        sys.exit(USAGE)
    data1,data2 = readData(label1,label2)
    tscores = computeTscore(data1,data2)
    writeData(tscores,data1,data2)
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
