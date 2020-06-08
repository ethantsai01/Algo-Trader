import requests
from bs4 import BeautifulSoup
from algo import preMarketAlgo




#returns true if there is no duplicates
def checkforDuplicates(listofElem, newElem):
    for x in listofElem:
        if newElem == x:
            return False
    return True        


#creates list based on ticker symbol from news in seekingalpha.com
def createList():
    #empty list
    stockList = []

    #data scaper
    r = requests.get("https://seekingalpha.com/market-news/all")
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all('li', {'class': "mc"})

    #finds only the ticker symbols
    for i in range(len(div)):
        temp = div[i].find('div', {'class': "media-left"})
        if temp != None: #checks if null
            if temp.text.strip() != "": #checks if empty
                if checkforDuplicates(stockList, temp.text):
                    stockList.append(str(temp.text))

    print(stockList) 
    return stockList


def finalWatchlist():
    #creates list from list.py
    watchlist = createList()

    #user input ticker symbols to add to watchlist
    response = ""
    while response != "done":
        response = raw_input("Input stocks you want to watch, type 'done' if you don't: ")
        
        if checkforDuplicates(watchlist, response):
            watchlist.insert(0,response)

        print("")  

    return watchlist

    
    
   



         