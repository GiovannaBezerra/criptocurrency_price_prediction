# Cryptocurrency Price Prediction with AUTO TS

# 'description': 'Bitcoin (BTC) is a cryptocurrency . Users are able to generate BTC through the process of mining. 
# Bitcoin has a current supply of 19,257,443. The last known price of Bitcoin is 17,217.46558683 USD and is up 0.17 
# over the last 24 hours. It is currently trading on 9923 active market(s) with $17,485,048,158.87 traded over the last 24 hours. 
# More information can be found at https://bitcoin.org/.',

#https://thecleverprogrammer.com/2021/12/27/cryptocurrency-price-prediction-with-machine-learning/

# To do:
# 1. Source:https://finance.yahoo.com/
# 2. API: https://github.com/ranaroussi/yfinance; https://pypi.org/project/yfinance/
# 3. Get and process data
# 4. Create graph visualization
# 5. Create predict model using AUTO TS
# 6. Split data test and train
# 7. Compare results to verify accuracy...
# 8. Create a dashboard to show results


# Import modules:
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

# Get and process data:
btc = yf.Ticker('BTC-USD')
print(btc)

# Description about Bitcoin:
print(btc.info['description'])

# Create a history price data frame:
df_btc = btc.history(period="max")

# Rename columns:
df_btc = df_btc.rename({'Open':'open', 'High':'high', 'Low':'low', 'Close':'close', 'Volume':'volume', 
                        'Dividends':'dividends', 'Stock Splits':'stock_splits'}, axis=1)

# Add column with date information and reset index:
df_btc['date'] = df_btc.index
df_btc.reset_index(drop=True, inplace=True)

# Rearrange columns order:
df_btc = df_btc[['date','open', 'high', 'low', 'close', 'volume', 'dividends', 'stock_splits']]

# Print first ten rows:
print(df_btc.head(10))

# Check missing values:
print(df_btc.info())

# First date price record:
print(min(df_btc.date))

# Last date price record:
print(max(df_btc.date))

# Graph:

