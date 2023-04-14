# Cryptocurrency Get Data:

# This program gets data from YAHOO! FINANCE using yfinance API (https://pypi.org/project/yfinance/). 
# After collecting and processing data, the data set is available for creating predictions and various types of visualizations.

# Historical OHLCV (Open High Low Close Volume) data are obtained:
# 1. date: date index
# 2. open: opening price
# 3. high: highest price
# 4. low: lowest price
# 5. close: close price
# 6. volume: trade volume

# Import modules:
import pandas as pd
import yfinance as yf

# Getting data from yfinance:
btc = yf.Ticker('BTC-USD')

# Creating history price data frame since 2021:
df_btc = btc.history(start='2021-01-01',actions=False)

# Adding column with date information and reset index:
df_btc['date'] = df_btc.index
df_btc.reset_index(drop=True, inplace=True)

# Renaming columns:
df_btc.rename(columns= str.lower, inplace = True)

# Rearranging columns order:
df_btc = df_btc[['date','open', 'high', 'low', 'close', 'volume']]

# Date converting type and remove timezone:
df_btc.date = pd.to_datetime(df_btc.date)
df_btc.loc[:, 'date'] = df_btc['date'].dt.tz_localize(None)

# Checking missing values:
missing_values=0
for col_name in df_btc.columns:
    if df_btc[col_name].isnull().sum() != 0:
        missing_values = missing_values + df_btc[col_name].isnull().sum()
        
# Printting missing values:
print('There are {} missing values on Data frame'.format(missing_values))

# Printting df shape:
print('Data frame shape: {}'.format(df_btc.shape))

print('Data frame extraction from {:%Y-%m-%d} to {:%Y-%m-%d}'.format(df_btc.date.min(),df_btc.date.max()))

# Printting result of running the program:
print('cryptocurrency_get_data successfully run')
