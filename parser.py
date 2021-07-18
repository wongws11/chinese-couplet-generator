fh = open('text.txt')

textList = []
for i in fh:
    i = i.split(' ')
    if len(i) > 2:
        continue
    elif i == ['\n']:
        continue
    else:
        textList.append(i)

#List with tone's metadata
textListMeta = []
tone = str()
for i in textList:
    if len(i) == 1:
        tone = i[0].replace('\n', '').replace('《', '').replace('》', '')
    else:
        textListMeta.append([i[1].replace('\n', '').replace('\t', ''), tone])

#List of tones
toneList = []
for i in textListMeta:
    if i[1] in toneList:
        continue
    else: toneList.append(i[1])

for i in toneList:
    for verse in textListMeta:
        if verse[1] == i:
            print(verse)
    print('\n')