import pandas as pd
import datetime as dt

# Adapted from https://github.com/jupyter-naas/drivers/blob/main/naas_drivers/tools/yahoofinance.py
def get_ticker(ticker: str):
    """
    Takes the ticker (a string) from Yahoo Finance,
    Adjusts interval to daily, 
    date_from to 1994 (days = -10000),
    date_to to today.
    Returns a pandas dataframe with ticker's stock data. 
    """
    ticker = ticker
    interval = "1d"
    date_from = dt.datetime.today() + dt.timedelta(days=-10000)
    date_to = dt.datetime.today()
    period1 = int(date_from.timestamp())
    period2 = int(date_to.timestamp())
    url = (
            f"https://query1.finance.yahoo.com/v7/finance/download/"
            f"{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history"
          )
    df = pd.read_csv(url).dropna()
    return df
    