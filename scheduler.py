from datetime import date, datetime
import schedule
import time



def findTime():
    time = datetime(2020, 1, 1, 8, 30) #8:30am CST
    temp = datetime.now()
    while temp <= time:
        temp = datetime.now().time()
        print(temp)
    return temp


def timer():
    #finds day of week
    today = date.today().weekday()
    print(today)

    #runs until market opens
    currentTime = findTime()
    print(currentTime.time())

    #scheduler
    if today == 0 or today == 1 or today == 2 or today == 3 or today == 4 or today == 5:
        return 1
    else:
        return 0

   
