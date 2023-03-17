# Cryptocurrency Model Building:

# This program build a model to predict Bitcoin prices using AUTO TS. 
# AUTO TS is an open-source python library used to automate Time Series Forecasting. It can automatically train multiple 
# time series models using a single line of code. 
# Source: https://www.analyticsvidhya.com/blog/2021/04/automate-time-series-forecasting-using-auto-ts/

# The data was splited into train and test (considering 80:20 ratio). 
# To simplify the model, was considered historical prices from YFinance since 2021.

# Import modules:
import pandas as pd
from autots import AutoTS

# Getting data from file cryptocurrency_get_data.py:
exec(open('cryptocurrency_get_data.py').read())

### Splitting training and test data:

# Using just the feature named "close" which is the daily closing price:
df = df_btc[["date", "close"]]

# Sortting values by date:
df = df.sort_values('date')

# Using ratio 80:20 to split test and train data. It means 80% of the data for training and 20% for test:
count_lines = df.shape[0]
limit = int(count_lines*0.8)

# Splitting train-test dataset:
train = df.iloc[:limit]
test = df.iloc[limit:]

### Building the model:

# Setting model parameters: 
model = AutoTS(forecast_length=test.shape[0],frequency='infer', ensemble='simple')

# Fitting model:
model = model.fit(train, date_col='date', value_col='close', id_col=None)