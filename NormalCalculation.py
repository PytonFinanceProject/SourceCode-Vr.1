import pandas as pd
from scipy.stats import norm
import scipy.stats as stats
import matplotlib.pyplot as plt
from statistics import NormalDist
import numpy as np


csv = "CSV/IT_Ratio.csv"
stats = "CSV/IT_Industry_Statistics.csv"
norm = "CSV/IT_NormalDistribution.csv"
def ReadCSV(csv):
    df = pd.read_csv(csv,index_col=0)
    df.dropna(how="all", inplace=True)
    return df

def normCal(mean, sd, value):
    return(NormalDist(mu=mean, sigma=sd).cdf(value))

def loopNorm(csv,stats):
    df = ReadCSV(csv)
    st = ReadCSV(stats)
    norm = {}
    for company in df.index:
        print(company)
        norm[company] = {}
        norm[company]['ROE']  = normCal(st['Median']['ROE'],st['MAD']['ROE'],df.loc[company,'ROE'])
        norm[company]['ROA']  = normCal(st['Median']['ROA'],st['MAD']['ROA'],df.loc[company,'ROA'])
        norm[company]['Debt_Ratio']  = 1 - normCal(st['Median']['Debt_Ratio'],st['MAD']['Debt_Ratio'],df.loc[company,'Debt_Ratio'])
        norm[company]['Interest_Coverage']  = normCal(st['Median']['Interest_Coverage'],
                                                      st['MAD']['Interest_Coverage'],df.loc[company,'Interest_Coverage'])
        norm[company]['Asset_Turnover']  = normCal(st['Median']['Asset_Turnover'],st['MAD']['Asset_Turnover'],df.loc[company,'Asset_Turnover'])
        norm[company]['Current_Ratio']  = normCal(st['Median']['Current_Ratio'],
                                                        st['MAD']['Current_Ratio'],df.loc[company,'Current_Ratio'])
        norm[company]['Gross_Profit_Margin']  = normCal(st['Median']['Gross_Profit_Margin'],
                                                        st['MAD']['Gross_Profit_Margin'],df.loc[company,'Gross_Profit_Margin'])
        norm[company]['Revenue_Growth']  = normCal(st['Median']['Revenue_Growth'],st['MAD']['Revenue_Growth'],df.loc[company,'Revenue_Growth'])
        norm[company]['NetIncome_Growth']  = normCal(st['Median']['NetIncome_Growth'],st['MAD']['NetIncome_Growth'],df.loc[company,'NetIncome_Growth'])
        norm[company]['RD_Growth']  = normCal(st['Median']['RD_Growth'],st['MAD']['RD_Growth'],df.loc[company,'RD_Growth'])

    DF = pd.DataFrame.from_dict(norm,orient='index')
    print(DF)
    DF.to_csv('IT_NormalDistribution.csv')
def graphNormal():
    mu = 0.1794323510
    sigma = 0.15112407
    x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
    plt.plot(x, norm.pdf(x, mu, sigma))
    plt.show()
    
def getScore(norm):
    df = ReadCSV(norm)
    score = {}
    for company in df.index:
        score[company] = {}
        score[company]['Innovation']  = df.loc[company,'RD_Growth']*15
        score[company]['Earning']  = (df.loc[company,'ROE']*.4 + df.loc[company,'Gross_Profit_Margin']*.4 + df.loc[company,'ROE']*.2)*25
        score[company]['Risk']  = (df.loc[company,'Debt_Ratio']*.4 + df.loc[company,'Current_Ratio']*.4 + df.loc[company,'Interest_Coverage']*.2)*25
        score[company]['Performance']  = (df.loc[company,'Asset_Turnover']*(15/35)+df.loc[company,'Revenue_Growth']*(10/35)
                                          +df.loc[company,'NetIncome_Growth']*(10/35))*35
        score[company]['Total']  =  score[company]['Performance']  + score[company]['Risk'] +  score[company]['Earning'] + score[company]['Innovation'] 
    DF = pd.DataFrame.from_dict(score,orient='index')
    print(DF)
    DF.to_csv('IT_Score.csv')
#graphNormal()
loopNorm(csv,stats)
getScore(norm)

