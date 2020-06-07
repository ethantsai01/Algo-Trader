from algo import algorithm
from list import createList
import schedule
import time

list = createList()

#execute algorithm
def do_loop():
    for i in list:
        algorithm(i)


#scheduler
schedule.every(5).seconds.do(do_loop)

#infinite timer
while True:
    schedule.run_pending()
    time.sleep(1)