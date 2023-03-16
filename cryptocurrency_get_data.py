# Cryptocurrency Get Data:

# Import modules:
import pandas as pd
import yfinance as yf

# Getting data from yfinance API (https://pypi.org/project/yfinance/):
btc = yf.Ticker('BTC-USD')

# Creating history price data frame since 2021:
df_btc = btc.history(start="2021-01-01")

# Adding column with date information and reset index:
df_btc['date'] = df_btc.index
df_btc.reset_index(drop=True, inplace=True)

# Renaming columns:
df_btc.rename(columns= str.lower, inplace = True)

# Rearranging columns order:
df_btc = df_btc[['date','open', 'high', 'low', 'close', 'volume', 'dividends', 'stock splits']]

# Date converting type:
df_btc.date = pd.to_datetime(df_btc.date)

# Checking missing values:
missing_values=0
for col_name in df_btc.columns:
    if df_btc[col_name].isnull().sum() != 0:
        missing_values = missing_values + df_btc[col_name].isnull().sum()
        
# Printting missing values:
print('There are {} missing values on Data frame'.format(missing_values))

# Printting df shape:
print('Data frame shape: {}'.format(df_btc.shape))

# Printting result of running the program:
print('cryptocurrency_get_data successfully run')