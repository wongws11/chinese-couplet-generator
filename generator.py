oneList = []
twoList = []
threeList = []
with open('oneWord.txt') as fh:
    for i in fh:
        oneList.append(i.split())
with open('twoWord.txt') as fh:
    for i in fh:
        twoList.append(i.split())
with open('threeWord.txt') as fh:
    for i in fh:
        threeList.append(i.split())

import random

def simple7():
    firstPair = random.choice(twoList)
    secondPair = random.choice(twoList)
    finalPair = random.choice(threeList)
    upper = firstPair[1] + secondPair[0] + finalPair[1]
    lower = firstPair[0] + secondPair[1] + finalPair[0]
    print(upper, lower)

for i in range(10):
    simple7()