import requests
from bs4 import BeautifulSoup


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

    return stockList





         