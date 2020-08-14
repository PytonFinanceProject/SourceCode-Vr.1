
#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import os
import pandas as pd

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

api = '82e40a70ff99dc31eeadf319d9792376'

def get_BalanceSheet(ticker,industry):
    url = "https://financialmodelingprep.com/api/v3/balance-sheet-statement/"+ ticker + "?apikey=" + api
    data = get_jsonparsed_data(url)
    if not os.path.exists('BalanceSheet/' + industry):
        os.makedirs('BalanceSheet/' + industry)
    df = pd.DataFrame(data)
    df.to_csv("BalanceSheet/" + industry + "/" +ticker + "_BalanceSheet" + ".csv")

def get_IncomeStatement(ticker,industry):
    url = "https://financialmodelingprep.com/api/v3/income-statement/"+ ticker + "?apikey=" + api
    data = get_jsonparsed_data(url)
    if not os.path.exists('IncomeStatement/' + industry):
        os.makedirs('IncomeStatement/' + industry)
    df = pd.DataFrame(data)
    df.to_csv("IncomeStatement/" + industry + "/" +ticker + "_IncomeStatement" + ".csv")

def get_CashFlow(ticker,industry):
    url = "https://financialmodelingprep.com/api/v3/cash-flow-statement/" + ticker + "?apikey=" + api
    data = get_jsonparsed_data(url)
    print (data)
    if not os.path.exists('CashFlow/' + industry):
        os.makedirs('CashFlow/' + industry)
    pd.read_json(json.dumps(data)).to_csv('CashFlow/' + industry + "/" + ticker + "_CashFlow" + ".csv")

def get_Ratios(ticker,industry):
    url = "https://financialmodelingprep.com/api/v3/financial-ratios/" + ticker + "?apikey=" + api
    data = get_jsonparsed_data(url)
    if not os.path.exists('Ratios/' + industry):
        os.makedirs('Ratios/' + industry)
    df = pd.DataFrame(data)
    df.to_csv('Ratios/' + industry + "/" + ticker + "_Ratios" + ".csv",sep = "," , header=False)

get_Ratios('AAPL','tech')
#get_CashFlow('AAPL','tech')
