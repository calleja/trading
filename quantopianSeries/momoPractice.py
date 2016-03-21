# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:24:48 2016
@author: lechuza

Momentum strategies are valuable to traders when they can take advantage of "motion", not price.
"""

import Quandl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels import regression
import sys
#sys.path.append('G:/Property/Luis_C/statsLearning')
sys.path.append('/home/lechuza/Documents/economicAnalysis/trading')

'''import all my datesets/price series '''
maaa = Quandl.get("MOODY/DAAAYLD", returns="pandas", trim_start="2014-01-02", trim_end="2016-02-20")

#should track closely with the US AA-rated Bond Index OAS:
ml_aaoas = Quandl.get("ML/AAOAS", returns="pandas", trim_start="2015-01-02")

#appears to be an index based on daily total returns
# S&P U.S. Issued AA Investment Grade Corporate Bond Index
spaaa = Quandl.get("SPDJ/SPUSG2AT", trim_start="2014-01-02", trim_end="2016-02-20")

#ML HY OAS
mlhyoas = Quandl.get("ML/HYOAS", trim_start="2014-01-02")
#SPY futures continuous contract
spy = Quandl.get("CHRIS/CME_SP1", trim_start="2014-01-02")

jwn=Quandl.get("WIKI/JWN",trim_start='2014-01-02',returns="pandas")
''' finito '''

jwn_eod=jwn['Close']
dates=pd.date_range(start=min(jwn_eod.index),end=max(jwn_eod.index),freq='5M')

#create a date array for the x axis labels... check out matplotlib.dates
#arguments need to be datetime instances; longest timedelta period is weeks (can't do months)
mdiz=mdates.drange(min(jwn_eod.index),max(jwn_eod.index),dt.timedelta(weeks=6))


#version a
#set up the axes and figure
fig,ax=plt.subplots()
ax.plot(jwn_eod)
ticks = ax.get_xticks()

#version b
plt.plot(jwn_eod.index,jwn_eod.values)
plt.xticks(dates)

#version c
fig,ax=plt.subplots()
ax.plot(jwn_eod)
ticks=ax.get_xticks() #doesn't work - returns a small list of length 8
fig.autofmt_xdate()
plt.show()

#makes space for and rotate the x-axis tick labels
fig.autofmt_xdate()
plt.show()

''' from momentum iPython Notebook '''
_, ax = plt.subplots()
ax.plot(asset)
ticks = ax.get_xticks()
ax.set_xticklabels([dates[i].date() for i in ticks[:-1]]) # Label x-axis with dates

# Find the line of best fit to illustrate the trend

'''running version 'C' from above and trying to overlay the below on the graph...
the X,Y,Y_hat variables all look good, but they do not overlay. The X variable
is not a date format, whereas the x-axis to the stock price chart is... 
The momentum notebook uses numbers for the x-axis and relabels 
as a date format later - that's why it works on the notebook'''

X = np.arange(len(jwn))
x = sm.add_constant(X) # Add a column of ones so that line can have a y-intercept
model = regression.linear_model.OLS(jwn_eod, x).fit()
a = model.params[0] # Get coefficients of line
b = model.params[1]
Y_hat = X * b + a
plt.plot(X, Y_hat, 'r', alpha=0.9)
plt.ylabel('Price')
plt.legend(['JWN', 'Trendline']);
''' finito '''

#recommend testing for autocorrelation
#use statsmodels.tsa.stattools import adfuller
#run something like _, pvalue, _, _, _, _ = adfuller(dataset)
'''augmented Dickey-Fuller test used to test for a unit root in a univariate 
process in the presence of serial correlation... 
the test has an associated p-value. 
Unit root aka "stochastic trend process". Note that standard deviation becomes 
contaminated with the presence of autocorrelation. And statistical 
tests that rely on s.d., like z-tests, t-tests, will not be correct'''

from statsmodels.tsa.stattools import adfuller
#make a numpy series/array out of the date index
ml_series=np.array(mlhyoas.index,dtype=pd.Series)
type(ml_series)
type(X)
_, pvalue, _, _, _, _=adfuller(ml_series)
print(pvalue) #extremely high MacKinnon's approximate p-value of 1, so we reject the null hypothesis, hence there is no unit root and no serial correlation... this isn't the end-all-be-all: there can be periods of trading that do experience autocorrelation. I will leave that to another study

'''check whether the security adheres more to mean reversion or momentum... 
make a decision before building a test on whether I think the asset 
will adhere to momentum or mean-reversion'''

'''Testing over varying time frames: I can run the Dickey-Fuller test over 
different time frames, and plot a histogram of the p-values'''

#multiple subplots: http://snowball.millersville.edu/~adecaria/ESCI386P/esci386-lesson12-Multiple-Panels.pdf

spy_last=spy.iloc[:,3] #daily closing prices
mlOAS=mlhyoas.iloc[:,0] # ~daily closing OAS


fig,ax=plt.subplots(2,1,figsize=(12,3)) #watch the arguments to subplots

ax[0].plot(mlOAS)
#fig.autofmt_xdate()
#plt.show()

#overlay continuous SPY futures prices

 #figure #2 of a grid of graphs having 2 rows and 1 columns
ax[1].plot(spy_last) #replaces plt.subplot(2,1,2)
fig.autofmt_xdate()
plt.show()



#this works
fig,ax=plt.subplots() #watch the arguments
ax.plot(mlOAS)
fig.autofmt_xdate()
plt.show()