#Reading the text
textList = []
with open('ctext.txt', 'r') as fh:
    for i in fh:
        textList.append(i.replace('\n', ''))

#Getting the pairs
oneWord = []
twoWord = []
threeWord = []

for i in textList:
    if '對' in i:
        if len(i) == 10:
            twoWord.append(i[:5].split('對'))
            twoWord.append(i[5:].split('對'))
            continue
        elif len(i) == 11:
            if i[1] == '對':
                oneWord.append(i[0:3].split('對'))
                oneWord.append(i[3:6].split('對'))
                twoWord.append(i[6:11].split('對'))
                continue
            else: 
                threeWord.append([i[0:3], i[3:6]])
                twoWord.append(i[6:11].split('對'))
    else: 
        if len(i) == 9:
            upperIndex = textList[textList.index(i) - 1]
            lowerIndex = textList[textList.index(i) + 1]
            if len(upperIndex) == 9:
                continue
            else: 
                twoWord.append([i[0:2], lowerIndex[0:2]])
                twoWord.append([i[2:4], lowerIndex[2:4]])
                oneWord.append([i[4:5], lowerIndex[4:5]])
                twoWord.append([i[5:7], lowerIndex[5:7]])
                twoWord.append([i[7:9], lowerIndex[7:9]])
        elif len(i) == 10:
            upperIndex = textList[textList.index(i) - 1]
            lowerIndex = textList[textList.index(i) + 1]
            if len(upperIndex) != 10 and len(lowerIndex) != 10:
                twoWord.append([i[0:2], i[5:7]])
                threeWord.append([i[2:5], i[7:10]])
            else:
                if len(lowerIndex) == 10:
                    twoWord.append([i[0:2], lowerIndex[0:2]])
                    twoWord.append([i[2:4], lowerIndex[2:4]])
                    twoWord.append([i[4:6], lowerIndex[4:6]])
                    twoWord.append([i[6:8], lowerIndex[6:8]])
                    twoWord.append([i[8:10], lowerIndex[8:10]])

# print(oneWord)
# print(twoWord)
# print(threeWord)

import random

def randomPairs(wordCount):
    k = random.randint(0, 1)
    if wordCount == 5:
        first = random.choice(twoWord)
        if k == 0:
            second = random.choice(threeWord)
            upperPair = str(first[0]) + str(second[0])
            lowerPair = str(first[1]) + str(second[1])
        elif k == 1:
            second = random.choice(oneWord)
            thrid = random.choice(twoWord)
            upperPair = str(first[0]) + str(second[0]) + str(thrid[0])
            lowerPair = str(first[1]) + str(second[1]) + str(thrid[1])
        print(upperPair, lowerPair)

    if wordCount == 7:
        first = random.choice(twoWord)
        second = random.choice(twoWord)
        if k == 0:
            thrid = random.choice(threeWord)
            upperPair = str(first[0]) + str(second[0]) + str(thrid[0])
            lowerPair = str(first[1]) + str(second[1]) + str(thrid[1])
        elif k == 1:
            thrid = random.choice(oneWord)
            forth = random.choice(twoWord)
            upperPair = str(first[0]) + str(second[0]) + str(thrid[0]) + str(forth[0])
            lowerPair = str(first[1]) + str(second[1]) + str(thrid[1]) + str(forth[1])
        print(upperPair, lowerPair)

for i in range(10):
    randomPairs(5)

for i in range(10):
    randomPairs(7)