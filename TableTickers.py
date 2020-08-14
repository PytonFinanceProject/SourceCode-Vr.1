import bs4 as bs
import pandas as pd
import urllib.request
import requests

#source = urllib.request.urlopen('https://www.barchart.com/stocks/indices/sp-sector/health-care').read()
url = 'https://www.tradingview.com/symbols/SP-S5COND/components/'
Industry = 'CD'
def readIndustryData(url,Industry):
    tickers = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    result = requests.get(url, headers=headers).content
    soup = bs.BeautifulSoup(result, "lxml")
    table = soup.find('table', {'class':'tv-data-table tv-screener-table'})
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('a')[0].text.replace('.', '-')
        tickers.append(ticker)
        print(ticker)
    df = pd.DataFrame(tickers)
    df.to_csv("Tickers/" + Industry + "_Tickers.csv")
    
readIndustryData(url,Industry)
