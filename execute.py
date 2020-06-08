from algo import preMarketAlgo
from list import finalWatchlist
from scheduler import timer
from datetime import date
import schedule
import time

#execute algorithm
def do_loop():
    for i in myWatchList:
        preMarketAlgo(i)

myWatchList = finalWatchlist()
checkToContinue = timer()

if checkToContinue == 1:
    schedule.every(5).seconds.do(do_loop)
    
#infinite timer
while True:
    schedule.run_pending()
    time.sleep(1)