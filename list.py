import requests
from bs4 import BeautifulSoup
from algo import preMarketAlgo


#returns true if there is no duplicates
def checkforDuplicates(listofElem, newElem):
    for x in listofElem:
        if newElem.upper() == x:
            return False
    return True        



#creates list
def createList():
    #empty list
    stockList = []

    #data scaper based on ticker symbol from news on seekingalpha.com
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


    #data scaper based on companies announcing earnings on that day
    r = requests.get("https://finance.yahoo.com/calendar/earnings/")
    html = r.text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all('a', {'class': "Fw(600) C($linkColor)"})
    
    for i in range(len(div)):
        temp = div[i].text
        if temp != None: #checks if null
            if checkforDuplicates(stockList, temp):
                 stockList.append(str(temp))


    print(stockList) 
    return stockList


#user input ticker symbols to add to watchlist
def finalWatchlist():
    #creates list from list.py
    watchlist = createList()

    #user input
    response = ""
    while response != "done":
        response = raw_input("Input stocks you want to watch, type 'done' if you don't: ")
        
        if checkforDuplicates(watchlist, response):
            watchlist.insert(0,response.upper())

        print("")  

    return watchlist


#checks if more ticker symbols were added to seekingalpha.com
def updateStocklist(currentList):
    addedTicker = []

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
                if checkforDuplicates(currentList, temp.text):
                    currentList.append(str(temp.text))

    #checks if addedTicker is empty
    if len(addedTicker) != 0:
        print("Adding:")
        print(addedTicker) 
        print("")

    return currentList

