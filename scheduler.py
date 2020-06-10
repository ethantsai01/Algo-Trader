from datetime import date, datetime
import schedule
import time



def findTime():
    time = datetime(2020, 1, 1, 8, 30) #8:30am CST
    temp = datetime.now()
    while temp <= time:
        temp = datetime.now().time()
    return temp


def timer():
    #finds day of week
    today = date.today().weekday()

    #runs until market opens
    currentTime = findTime()

    #scheduler
    if today <= 5:
        return 1
    else:
        return 0

   
