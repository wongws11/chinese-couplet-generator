import csv

pingFile = open("list.tsv", "r")
pingReader = csv.reader(pingFile, delimiter="\t")

def searchList(char):
    pingFile.seek(0)
    for i in pingReader:
        if i[0] == char:
            return i

def searchChar(pingyam):
    pingFile.seek(0)
    charList = []
    for i in pingReader:
        if i[2] == pingyam:
            charList.append(i[0])
    return "/".join(charList)

# 上字取聲下字取韻
def faancit(words):
    if len(words) != 2:
        print("Error: input string must be two characters")
    else:
        upper = searchList(words[0])
        lower = searchList(words[1])

        #yamyeung
        if upper[5] == "1" or upper[5] == "2" or upper[5] == "3":
            upperYam = True
        else: upperYam = False
        if lower[5] == "1" or lower[5] == "2" or lower[5] == "3":
            lowerYam = True
        else: lowerYam = False

        stops = ["b", "p", "d", "t", "g", "k", "gw", "kw", "z", "c"]
        #upper stop
        if upper[3] in stops:
            upperStop = True
        else: upperStop = False

        #lower ping
        if lower[5] == "1" or lower[5] == "4":
            lowerPing = True
        else: lowerPing = False

        #sing
        if upperYam is False and upperStop is True:
            if lowerPing is True:
                if upper[3] == "b" or upper[3] == "p":
                    sing = "p"
                if upper[3] == "d" or upper[3] == "t":
                    sing = "t"
                if upper[3] == "g" or upper[3] == "k":
                    sing = "k"
                if upper[3] == "gw" or upper[3] == "kw":
                    sing = "kw"
                if upper[3] == "z" or upper[3] == "c":
                    sing = "c"
            elif lowerPing is False:
                if upper[3] == "b" or upper[3] == "p":
                    sing = "b"
                if upper[3] == "d" or upper[3] == "t":
                    sing = "d"
                if upper[3] == "g" or upper[3] == "k":
                    sing = "g"
                if upper[3] == "gw" or upper[3] == "kw":
                    sing = "gw"
                if upper[3] == "z" or upper[3] == "c":
                    sing = "z"
        else: sing = upper[3]

        #wan
        wan = lower[4]

        fricative = ["f", "s", "h"]
        # Tone
        if upperYam is True and lowerYam is False:
            # print("上字陰下字陽")
            tone = str(int(lower[5]) - 3)
        elif upperYam is False and lowerYam is True:
            # print("上字陽下字陰")
            tone = str(int(lower[5]) + 3)
        else: 
            # print("上下字陰陽相等")
            tone = lower[5]

        if upperYam is False and (upper[3] in stops or upper[3] in fricative):
            if tone == "2":
                tone = "3"
            elif tone == "5":
                tone = "6"

        pingyam = sing + wan + tone
        return pingyam, searchChar(pingyam)

print(faancit("承紙"))