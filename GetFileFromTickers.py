import pandas as pd
import numpy as np
import Get_CSV_From_API as api
import os
from yahoofinancials import YahooFinancials

csv = "Tickers/CD_Tickers.csv"

#Convert CSV to numpy Array
def LoopCSV(csv):
    df = pd.read_csv(csv,usecols=["0"])
    df.dropna(how="all", inplace=True)
    tickers = df.to_numpy()
    return tickers



def downloadDataFromTickers(tickers,filetype):
    if not os.path.exists('stock'):
        os.makedirs('stock')
    for ticker in tickers:
        nt = str (ticker).replace("['", '')
        newticker = str (nt).replace("']", '')
        print(newticker)
        if filetype =='balance':
            api.get_BalanceSheet(newticker,"Utility")
        if filetype == 'income':
            api.get_IncomeStatement(newticker,"Utility")
        if filetype == 'cash':
            api.get_CashFlow(newticker,"Utility")

downloadDataFromTickers(LoopCSV(csv),'income')
