from algo import preMarketAlgo
from list import finalWatchlist, updateStocklist
from scheduler import timer
from datetime import date
import schedule
import time

#execute algorithm
def do_loop():
    updateWatchlist = updateStocklist(myWatchlist)
    for i in updateWatchlist:
        preMarketAlgo(i)
    print("=================\n")
    

myWatchlist = finalWatchlist()
checkToContinue = timer()

if checkToContinue == 1:
    schedule.every(5).seconds.do(do_loop)
    
#infinite timer
while True:
    schedule.run_pending()
    time.sleep(1)