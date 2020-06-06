from algo import algorithm
import schedule
import time

list = ['msft', 'aapl', 'ba', 'xspa', 'twtr', 'goog']

#execute algorithm
def do_loop():
    for i in list:
        algorithm(i)


#scheduler
schedule.every(5).seconds.do(do_loop)

#timer
while True:
    schedule.run_pending()
    time.sleep(1)