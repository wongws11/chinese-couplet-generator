fh = open('text.txt')

rhymeList = []
tempList = []
for i in fh:
    i = i.replace('\n', '').split('\t')
    if len(i) == 1:
        rhyme = i
        rhymeList.append(rhyme[0])
    elif len(i) == 2:
        verse = i
        tempList.append([rhyme[0], verse[0], verse[1]])
# tempList = [head, num, verse]

largeDict = {}
for head in rhymeList:
    headDict = {}
    for i in tempList:
        if head == i[0]:
            headDict[i[1]] = i[2]
    largeDict[head] = headDict
# largeDict = {head: {num: verse}}

# 平聲level, 仄聲oblique
metaList = []
for head in rhymeList:
    verse = largeDict.get(head)
    metaList.append([verse.get('1')[0], verse.get('1')[2]])
    metaList.append([verse.get('1')[5], verse.get('1')[3]])
    metaList.append([verse.get('1')[9:11], verse.get('1')[6:8]])
    metaList.append([verse.get('2')[0:2], verse.get('2')[3:5]])
    metaList.append([verse.get('2')[8:10], verse.get('2')[5:7]])
    metaList.append([verse.get('3')[3:6], verse.get('3')[0:3]])
    metaList.append([verse.get('3')[9:11], verse.get('3')[6:8]])
    metaList.append([verse.get('4')[0:2], verse.get('4')[5:7]])
    metaList.append([verse.get('4')[7:10], verse.get('4')[2:5]])
    metaList.append([verse.get('5')[7:9], verse.get('5')[0:2]])
    metaList.append([verse.get('5')[2:4], verse.get('5')[9:11]])
    metaList.append([verse.get('5')[11:14], verse.get('5')[4:7]])
    metaList.append([verse.get('7')[0:2], verse.get('6')[0:2]])
    metaList.append([verse.get('6')[2:4], verse.get('7')[2:4]])
    metaList.append([verse.get('7')[4:6], verse.get('6')[4:6]])
    metaList.append([verse.get('6')[6:8], verse.get('7')[6:8]])
    metaList.append([verse.get('7')[8:10], verse.get('6')[8:10]])
    metaList.append([verse.get('8')[0], verse.get('8')[2]])
    metaList.append([verse.get('8')[5], verse.get('8')[3]])
    metaList.append([verse.get('8')[9:11], verse.get('8')[6:8]])
    metaList.append([verse.get('9')[0:2], verse.get('9')[3:5]])
    metaList.append([verse.get('9')[8:10], verse.get('9')[5:7]])
    metaList.append([verse.get('10')[3:6], verse.get('10')[0:3]])
    metaList.append([verse.get('10')[9:11], verse.get('10')[6:8]])
    metaList.append([verse.get('11')[0:2], verse.get('11')[5:7]])
    metaList.append([verse.get('11')[7:10], verse.get('11')[2:5]])
    metaList.append([verse.get('12')[7:9], verse.get('12')[0:2]])
    metaList.append([verse.get('12')[2:4], verse.get('12')[9:11]])
    metaList.append([verse.get('12')[11:14], verse.get('12')[4:7]])
    metaList.append([verse.get('14')[0:2], verse.get('13')[0:2]])
    metaList.append([verse.get('13')[2:4], verse.get('14')[2:4]])
    metaList.append([verse.get('14')[4:6], verse.get('13')[4:6]])
    metaList.append([verse.get('13')[6:8], verse.get('14')[6:8]])
    metaList.append([verse.get('14')[8:10], verse.get('13')[8:10]])
    metaList.append([verse.get('15')[0], verse.get('15')[2]])
    metaList.append([verse.get('15')[5], verse.get('15')[3]])
    metaList.append([verse.get('15')[9:11], verse.get('15')[6:8]])
    metaList.append([verse.get('16')[0:2], verse.get('16')[3:5]])
    metaList.append([verse.get('16')[8:10], verse.get('16')[5:7]])
    metaList.append([verse.get('17')[3:6], verse.get('17')[0:3]])
    metaList.append([verse.get('17')[9:11], verse.get('17')[6:8]])
    metaList.append([verse.get('18')[0:2], verse.get('18')[5:7]])
    metaList.append([verse.get('18')[7:10], verse.get('18')[2:5]])
    metaList.append([verse.get('19')[7:9], verse.get('19')[0:2]])
    metaList.append([verse.get('19')[2:4], verse.get('19')[9:11]])
    metaList.append([verse.get('19')[11:14], verse.get('19')[4:7]])
    metaList.append([verse.get('21')[0:2], verse.get('20')[0:2]])
    metaList.append([verse.get('20')[2:4], verse.get('21')[2:4]])
    if len(verse.get('20')) == 10:
        metaList.append([verse.get('21')[4:6], verse.get('20')[4:6]])
        metaList.append([verse.get('20')[6:8], verse.get('21')[6:8]])
        metaList.append([verse.get('21')[8:10], verse.get('20')[8:10]])
    # TODO add custom spilter

write1 = open('oneWord.txt', 'w')
write2 = open('twoWord.txt', 'w')
write3 = open('threeWord.txt', 'w')
for i in metaList:
    if len(i[0]) == 1:
        write1.write(i[0] + ' ' + i[1] + '\n')
        write1.close
    elif len(i[0]) == 2:
        write2.write(i[0] + ' ' + i[1] + '\n')
        write2.close
    elif len(i[0]) == 3:
        write3.write(i[0] + ' ' + i[1] + '\n')
        write3.close