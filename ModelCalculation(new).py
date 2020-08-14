import pandas as pd
import requests
import numpy as np
from scipy import stats

companies = []
csv = "Tickers/IT_Tickers.csv"
api = "82e40a70ff99dc31eeadf319d9792376"
ratio = "IT_Ratio.csv"

def LoopCSV(csv):
    df = pd.read_csv(csv,usecols=["0"])
    df.dropna(how="all", inplace=True)
    tickers = df.to_numpy()
    return tickers

def getDataFromTickers(tickers):
    for item in tickers:
        item = str(item).strip('\'[]\'')
        #print (item)
        companies.append(item)
    #print (companies)
    value_ratios ={}
    count = 0
    
    for company in companies:
        print (company)
        fin_ratios = requests.get('https://financialmodelingprep.com/api/v3/ratios/'+ company +'?apikey='+api).json()
        value_ratios[company] = {}
        value_ratios[company]['ROE'] = fin_ratios[0]['returnOnEquity']
        value_ratios[company]['ROA'] = fin_ratios[0]['returnOnAssets']
        value_ratios[company]['Debt_Ratio'] = fin_ratios[0]['debtRatio']
        value_ratios[company]['Interest_Coverage'] = fin_ratios[0]['interestCoverage']
        value_ratios[company]['Asset_Turnover'] = fin_ratios[0]['assetTurnover']
        value_ratios[company]['Current_Ratio'] = fin_ratios[0]['currentRatio']
        value_ratios[company]['Gross_Profit_Margin'] = fin_ratios[0]['grossProfitMargin']
        #more financials on growth:https://financialmodelingprep.com/api/v3/financial-growth/AAPL?apikey=demo
        growth_ratios = requests.get(f'https://financialmodelingprep.com/api/v3/financial-growth/'+ company +'?apikey='+api).json()
        value_ratios[company]['Revenue_Growth'] = growth_ratios[0]['revenueGrowth']
        value_ratios[company]['NetIncome_Growth'] = growth_ratios[0]['netIncomeGrowth']
        value_ratios[company]['RD_Growth'] = growth_ratios[0]['rdexpenseGrowth']
    DF = pd.DataFrame.from_dict(value_ratios,orient='index')    
    DF.to_csv("IT_Ratio.csv")
    print(DF)


def getStats (ratio):
    ratios_mean = {}
    DF = pd.read_csv(ratio)
    ratios_mean['ROE'] = DF['ROE'].median()
    ratios_mean['ROA'] = DF['ROA'].median()
    ratios_mean['Debt_Ratio'] = DF['Debt_Ratio'].median()
    ratios_mean['Interest_Coverage'] = DF['Interest_Coverage'].median()
    ratios_mean['Asset_Turnover'] = DF['Asset_Turnover'].median()
    ratios_mean['Current_Ratio'] = DF['Current_Ratio'].median()
    ratios_mean['Gross_Profit_Margin'] = DF['Gross_Profit_Margin'].median()
    ratios_mean['Revenue_Growth'] = DF['Revenue_Growth'].median()
    ratios_mean['NetIncome_Growth'] = DF['NetIncome_Growth'].median()
    ratios_mean['RD_Growth'] = DF['RD_Growth'].median()
    ## Absoulte Median Deviation
    ratio_dev = {}
    ratio_dev['ROE'] = mad(DF['ROE'])
    ratio_dev['ROA'] = mad(DF['ROA'])
    ratio_dev['Debt_Ratio'] = mad(DF['Debt_Ratio'])
    ratio_dev['Interest_Coverage'] = mad(DF['Interest_Coverage'])
    ratio_dev['Asset_Turnover'] = mad(DF['Asset_Turnover'])
    ratio_dev['Current_Ratio'] = mad(DF['Current_Ratio'])
    ratio_dev['Gross_Profit_Margin'] = mad(DF['Gross_Profit_Margin'])
    ratio_dev['Revenue_Growth'] = mad(DF['Revenue_Growth'])
    ratio_dev['NetIncome_Growth'] = mad(DF['NetIncome_Growth'])
    ratio_dev['RD_Growth'] = mad(DF['RD_Growth'])

    df = pd.DataFrame.from_dict(ratios_mean,columns = ['Median'],orient='index')
    df1 = pd.DataFrame.from_dict(ratio_dev,columns = ['Median_Absoulte_Deviation'],orient='index')
    result = pd.concat([df,df1],axis=1)

    print (result)
    result.to_csv("IT_Industry_Statistics.csv")

def mad(df):
    sd =  []
    median = df.median()
    for value in df:
        sd.append(abs(median - value))

    df = pd.DataFrame(sd)
    return(float (df.median()))

    

#DF = pd.read_csv(ratio)
#mad(DF ['ROE'])
getDataFromTickers(LoopCSV(csv))
getStats (ratio)

        
