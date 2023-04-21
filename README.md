<img src="https://user-images.githubusercontent.com/44107852/233521994-973b8bb0-7973-4eda-b5ef-78dc5cc2414a.png" align="right"
      width="70" height="70">
      
# Cryptocurrency Price Prediction with AUTO TS
   
   
This program aims to develop a machine learning model to predict Bitcoin prices using AUTO TS.

![candlestick_graph](https://user-images.githubusercontent.com/44107852/233504877-c678f7a7-a469-4107-aa42-3b40a1b591b3.jpg)

><img src="https://user-images.githubusercontent.com/44107852/232332112-330712e3-4ed0-4703-a88e-4fc4edbe68db.png" 
align="left" alt="imdb logo" width="20" height="20">
*This price model prediction can only work in situations where prices changes due to historical variation. Any other price variation reasons, such as government regulations, changes in financial policies, etc do not impact the presented predictions.*

## Table Of Content  

[1. Problem understanding](#1.-problem-understanding)  
[2. How to use](#2.-how-to-use)  
[3. Development steps](#3.-development-steps)    
[4. Results](#4.-results)  
[5. Notes and Considerations](#5.-notes-and-considerations)  


## 1. Problem understanding  

Cryptocurrency is a digital currency in which transactions are verified and records maintained by a decentralized system using cryptography, rather than by a centralized authority. In recent years, cryptocurrency trading has become more and more popular and can be considered a good way to invest because it offers great returns even in a short period.   

This work proposal is based on extracting meaningful patterns and attributes from historical cryptocurrency data to predict future prices using machine learning for time series. A time serie is a sequence of data points that occur in successive order over time.   

For this program we will use **Bitcoin**. Founded in 2009, it was the first cryptocurrency and remains one of the most popular today. More information can be found at https://bitcoin.org/.

## 2. How to use  

### Installation and configuration 

```
# Clone this repository
git clone https://github.com/GiovannaBezerra/cryptocurrency_price_prediction.git

# Install development dependencies
Requirements:
- pandas
- numpy
- matplotlib
- seaborn
- yfinance
- mplfinance
- dask
- sklearn
- statsmodels
- pmdarima
- xgboost
- prophet
- auto-ts 0.0.69
```

For Windows users, it is recommended to see the installation instructions in the [AUTO TS documentation](https://github.com/AutoViML/Auto_TS#note-for-windows-users).

After cloning the repository, two files must be saved: [cryptocurrency_getdata.py](https://github.com/GiovannaBezerra/cryptocurrency_price_prediction/blob/main/cryptocurrency_get_data.py), wich contains the source code to get data and [cryptocurrency_price_prediction.ipynb](https://github.com/GiovannaBezerra/cryptocurrency_price_prediction/blob/main/cryptocurrency_price_prediction.ipynb) which contains the data analysis on jupyter notebook.

## 3. Development steps

The work was divided into three main steps:   
> 1. Colect and process data
> 2. Model Building
> 3. Model Evaluation

In the first step, historical Bitcoin prices were collected from [YAHOO! FINANCE](https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch) using [yfinance API](https://pypi.org/project/yfinance/). Historical data for OHLCV (Open High Low Close Volume) was obtained since January, 2021 and has been cleaned and processed to create predictions and visualizations.   

To build the model were used historical prices of the last 60 days and the data set were splitted into training and testing considering the proportion of 90:10, that is, 90% of the data for training and 10% for testing.

![train-test](https://user-images.githubusercontent.com/44107852/233522145-7cdaaf11-9823-4406-b4a3-c5288c8d8350.jpg)

The model building parameters were defined in the second stage. For this analysis the **AUTO TS** library was used. AUTO TS is a complex model building utility for time series data. Since it automates many Tasks involved in a complex endeavor, it assumes many intelligent defaults. AUTO TS will automatically select the best model which gives best score specified. [See more](https://pypi.org/project/auto-ts/). 

Lastly, the results can be compared on the model evaluation step. To evaluate the model training results, the Root Mean Square Error (RMSE) was used. The best model obtained was AUTO_SARIMAX with 1,106.92 for RMSE score.

![training-result](https://user-images.githubusercontent.com/44107852/233522180-d3b92ac4-9369-43c2-b65d-d88490dcfd1e.jpg)

The model performance with test dataset was calculated comparing the test dataset (previously separated) and model predictions for the same period. In this case, 277.09 was obtained for the RMSE score, which means that the prediction can be wrong by an average of USD 277.09 (plus or minus). In relative terms, the model achieved 0.75% of MAPE score - mean absolute percentage difference between the actual and the predicted value.


## 4. Results 

In summary, the model that obtained the best performance - lowest RMSE- was **AUTO_SARIMAX**. This model is able to predict prices for the next 8 days with **277.09 for RMSE score** (average distance between the predicted and the actual values) and **0.75% for MAPE score** (mean of all absolute percentage errors between the predicted and actual values), considering evaluation with test data.

![test-result](https://user-images.githubusercontent.com/44107852/233242095-ce8bebde-2588-4cdd-a3f3-0e4aced02d94.jpg)

From the image above, the blue line shows the actual values, using for model training and validation. The red dotted line shows the values using for test and the orange line shows forecast values.


## 4. Notes and Considerations  

It is important to emphasize again that buying and selling trends depend on many factors and the model obtained is only capable of working with historical data.

This project was really challenging for me. I had the opportunity to learn more about web scraping and time series, as well as to develop new skills to build multiple machine learning models automatically.


### References

<https://github.com/matplotlib/mplfinance>   
<https://thecleverprogrammer.com/2021/12/27/cryptocurrency-price-prediction-with-machine-learning/>  
<https://www.analyticsvidhya.com/blog/2021/04/automate-time-series-forecasting-using-auto-ts/>  
<https://www.section.io/engineering-education/time-series-analysis-and-forecasting-using-auto-time-series/>   
