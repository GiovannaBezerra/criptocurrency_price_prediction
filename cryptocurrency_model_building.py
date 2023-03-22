# Cryptocurrency Model Building:

# This program build a model to predict Bitcoin prices using AUTO TS. 
# AUTO TS is an open-source python library used to automate Time Series Forecasting. It can automatically train multiple 
# time series models using a single line of code. 
# Source: https://www.analyticsvidhya.com/blog/2021/04/automate-time-series-forecasting-using-auto-ts/
# https://pypi.org/project/AutoTS/


# The data was splited into train and test (considering 90:10 ratio). 
# To simplify the model, was considered historical prices from YFinance since 2021.

# Import modules:
import pandas as pd
from autots import AutoTS

# Getting data from file cryptocurrency_get_data.py:
exec(open('cryptocurrency_get_data.py').read())

### Splitting training and test data:

# Sortting values by date:
df_btc = df_btc.sort_values('date')

# Select few date to run model:
df = df_btc.loc[df_btc.date >= '2023-01-01'].reset_index(drop=True)

# Using just the feature named "close" which is the daily closing price:
df = df[["date", "close"]]

# Using ratio 90:10 to split test and train data. It means 90% of the data for training and 10% for test:
count_lines = len(df.index)
limit = int(count_lines*0.9)

# Splitting train-test dataset:
train = df.iloc[:limit]
test = df.iloc[limit:]

### Building the model:

# Setting model parameters: 
model = AutoTS(forecast_length=int(len(test.index)),frequency='infer', ensemble='simple')

# Fitting model:
model = model.fit(train, date_col='date', value_col='close', id_col=None)
