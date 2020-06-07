from algo import algorithm
from list import createList, checkforDuplicates
import schedule
import time

#creates list from list.py
watchlist = createList()

#user input tickery symbols to add to watchlist
response = ""
while response != "done":
    response = raw_input("Input stocks you want to watch, type 'done' if you don't: ")
    
    if checkforDuplicates(watchlist, response):
        watchlist.insert(0,response)

#execute algorithm
def do_loop():
    for i in watchlist:
        algorithm(i)


#scheduler
schedule.every(5).seconds.do(do_loop)

#infinite timer
while True:
    schedule.run_pending()
    time.sleep(1)