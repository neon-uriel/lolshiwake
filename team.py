import random
def team(*names):
    namesList = list(names)
    raneList = ["TOP","JG","MID","AD","SUP"]
    sList = ["1 : ", "2 : "]
    team1 = []
    team2 = []
    cnt = len(names)
    if cnt == 8:
        random.shuffle(namesList)
        team2.append(str(str(raneList[0]) + str(sList[1]) + "."))
        for j in range(4):
            m = str(str(raneList[j+1]) + str(sList[1]) + str(namesList[j]))
            team2.append(m)
        team1.append(str(str(raneList[0]) + str(sList[0]) + "."))
        for i in range(4):
            m = str(str(raneList[i+1]) + str(sList[0]) + str(namesList[4+i]))
            team1.append(m)
        return (team1,team2)
    if cnt > 10:
        print("error")
        return
    if cnt < 10:
        for i in range(10 - cnt):
            namesList.append(".")
    random.shuffle(namesList)
    for j in range(5):
        m = str(str(raneList[j]) + str(sList[1]) + str(namesList[j]))
        team2.append(m)
    for i in range(5):
        m = str(str(raneList[i]) + str(sList[0]) + str(namesList[5+i]))
        team1.append(m)
    return (team1,team2)
def mikuji():
    raneList = ["TOP","JG","MID","AD","SUP"]
    random.shuffle(raneList)
    return raneList[0]

def team5(*names):
    namesList = list(names)
    raneList = ["TOP : ","JG : ","MID : ","AD : ","SUP : "]
    team1 = []
    cnt = len(names)
    if cnt > 5:
        print("error")
        return
    if cnt < 5:
        for i in range(5 - cnt):
            namesList.append(".")
    random.shuffle(namesList)
    for i in range(5):
        m = str(str(raneList[i]) + str(namesList[i]))
        team1.append(m)
    return (team1)
