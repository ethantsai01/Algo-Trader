import requests
from bs4 import BeautifulSoup



def algorithm(stock):
    
    #data scaper
    r = requests.get("https://finance.yahoo.com/quote/" + format(stock))
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    #finds current volume and avg volume
    div = soup.find_all('td', {'class': "Ta(end) Fw(600) Lh(14px)"})
    Volume = float(div[6].text.replace(',',''))
    avgVolume = float(div[7].text.replace(',',''))

    #volume %
    if Volume / avgVolume > 0.1:
        print("volume percent buy")
    else:
        print("volume percent DONT buy")



    #gap % from closing
    closingPrice = float(div[0].text.replace(',',''))
    div2 = soup.find_all('div', {'class' :"My(6px) Pos(r) smartphone_Mt(6px)"})
    ans = div2[0].text.split("+",1)
    currentPrice = float(ans[0].replace(',',''))

    if (currentPrice - closingPrice) / closingPrice > .2:
        print("gap percentage buy")
    else:
        print("gap percentage DONT buy")

