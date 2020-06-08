import requests
from bs4 import BeautifulSoup

def plusOrMinus(temp):
    if temp.find("+") > 0:
        return temp.split("+",1)
    if temp.find("-") > 0:
        return temp.split("-",1)
    if temp.find(".") > 0:
        return temp.rsplit(".",4)

def preMarketAlgo(stock):
    
    #data scaper
    r = requests.get("https://finance.yahoo.com/quote/" + format(stock))
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    #checks if ticker symbol exists
    div = soup.find_all('td', {'class': "Ta(end) Fw(600) Lh(14px)"})
    if not div:
        return
    else:
        if div[6].text == "N/A" or div[7].text == "N/A":
            return
        #finds current volume and avg volume
        Volume = float(div[6].text.replace(',',''))
        avgVolume = float(div[7].text.replace(',',''))

        #finds previous closing price and current price
        closingPrice = float(div[0].text.replace(',',''))
        div2 = soup.find_all('div', {'class' :"My(6px) Pos(r) smartphone_Mt(6px)"})
        ans = plusOrMinus(div2[0].text)
        currentPrice = ans[0].replace(',','')
        price = float(currentPrice)


        #volume % and gap %
        volumePercent = Volume / avgVolume
        gapPercent = (price - closingPrice) / closingPrice

        #thresholds
        if volumePercent > 0.1 and gapPercent > .2:
            print(stock.upper() + " at " + '\033[92m' + currentPrice + "\033[0m")
            print("Volume %: " + str(volumePercent))
            print("Gap %: " + str(gapPercent))
        else:
            return


    print("")


